# src/semantic_analyzer.py
# Minimalni semantički analizator za Swift → UML sekvence.
# Radi sa generisanim klasama iz tvoje gramatike (src/antlr_gen/SwiftParser*.py).

import re
from antlr4 import ParseTreeWalker
from src.antlr_gen.SwiftParserListener import SwiftParserListener  # generiše ga ANTLR

class SemanticAnalyzer(SwiftParserListener):
    """
    Šta radi:
      - Održava hijerarhiju scope-ova (global, func, block).
      - Deklariše var/let i parametre funkcija.
      - Heuristički prepoznaje konstrukcije tipa: let s = Service()  → s: Service.
      - Prijavljuje nedefinisana imena u izrazima, ali:
          * IGNORIŠE argument-labele (ime ispred ':', npr. key, id, amount...)
          * IGNORIŠE članove poslije tačke (a.b), i riječi koje počinju velikim slovom (pretpostavka: tip/namespace).
    Napomena: ovo nije pun Swift type checker — cilj je “dovoljno dobro” za generisanje UML sekvenci.
    """

    def __init__(self):
        self.errors = []
        self._scopes = []             # list[dict[str, dict(type=...)]]
        self._current_type = None
        self._builtins = {"print", "println"}  # proširi po potrebi

    # ---------- JAVNI API ----------
    def analyze(self, tree):
        self.errors = []
        self._scopes = [ {} ]         # global scope
        self._current_type = None
        ParseTreeWalker().walk(self, tree)
        return self.errors

    # ---------- SCOPE HELPERI ----------
    def _push(self):
        self._scopes.append({})

    def _pop(self):
        if self._scopes:
            self._scopes.pop()

    def _declare(self, name, typ=None):
        scope = self._scopes[-1]
        if not name:
            return
        if name in scope:
            self.errors.append(f"Dvostruka deklaracija lokalne promjenljive: '{name}'")
        scope[name] = {"type": typ}

    def _resolve(self, name):
        for scope in reversed(self._scopes):
            if name in scope:
                return scope[name]
        return None

    # ---------- HEURISTIKE / POMOĆNE ----------
    _ID_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")

    def _infer_type_from_ctor(self, expr_text: str):
        """
        Ako izraz izgleda kao TypeName(...), i TypeName počinje velikim slovom,
        tretiramo ga kao konstruktor i vraćamo 'TypeName'.
        """
        m = re.match(r"\s*([A-Z][A-Za-z0-9_]*)\s*\(", expr_text)
        return m.group(1) if m else None

    def _member_names_in(self, txt: str):
        # Imena koja se pojavljuju poslije . ili ?.
        return {m.group(1) for m in re.finditer(r"(?:\.|\?\.)\s*([A-Za-z_][A-Za-z0-9_]*)", txt)}

    def _strip_strings(self, txt: str):
        # Ukloni stringove da ne remete identifikatore
        txt = re.sub(r'"(?:\\.|[^"\\])*"', '""', txt)
        txt = re.sub(r"'(?:\\.|[^'\\])*'", "''", txt)
        return txt

    # ---------- KLJUČNI PATCH: ignorisanje argument-labela ----------
    def _check_expr_text(self, txt: str, where: str):
        """
        Heuristička provjera nedefinisanih imena u izrazu.
        Ne prijavljuj:
          - builtins, self, super, true/false/nil
          - članove poslije tačke (a.b) — 'b' je property/metoda
          - identifikatore koji počinju velikim slovom (pretpostavi tip/namespace)
          - ARGUMENT-LABELE ispred ':' unutar poziva (npr. key:, id:, amount:, name:, useCard:)
        """
        t = self._strip_strings(txt)

        # 1) imena članova poslije '.' ili '?.'
        member_names = self._member_names_in(t)

        # 2) argument-labele i ključevi (pattern: <ident> :)
        #    npr. request(path: "/x"), load(key: "u1"), pay(amount: 100)
        arg_labels = {m.group(1) for m in re.finditer(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*:", t)}

        for name in self._ID_RE.findall(t):
            # builtins / posebne riječi
            if name in self._builtins or name in {"self", "super", "true", "false", "nil"}:
                continue
            # vjerovatno ime tipa / namespace-a
            if name and name[0].isupper():
                continue
            # član iza tačke (a.**b**)
            if name in member_names:
                continue
            # argument-label (ime prije ':')
            if name in arg_labels:
                continue
            # nije pronađeno u scope-u → greška
            if not self._resolve(name):
                self.errors.append(f"Nedefinisani identifikator '{name}' u {where}")

    # ---------- LISTENER CALLBACKS (usaglašeno s tvojom gramatikom) ----------

    # typeDecl : (CLASS | STRUCT | ENUM | PROTOCOL | EXTENSION) IDENT typeBody ;
    def enterTypeDecl(self, ctx):
        self._current_type = ctx.IDENT().getText()

    def exitTypeDecl(self, ctx):
        self._current_type = None

    # funcDecl : FUNC IDENT paramClause returnClause? block
    def enterFuncDecl(self, ctx):
        # novi scope za parametre i lokale
        self._push()

        # HEURISTIKA: registruj imena parametara iz paramClause
        try:
            pcl = ctx.paramClause()
            if pcl:
                txt = pcl.getText()  # npr. "(amount:Int,id:Int)" ili "(ext name:String)"
                # skini zagrade
                content = txt[1:-1] if txt.startswith("(") and txt.endswith(")") else txt
                # razbij po zarezima
                for seg in [s.strip() for s in content.split(",") if s.strip()]:
                    # uzmi lijevu stranu do ':' i zadrži poslednji identifier (unutrašnje ime)
                    parts = seg.split(":")
                    if len(parts) >= 2:
                        left = parts[0].strip()
                        tokens = [t for t in re.findall(r"[A-Za-z_][A-Za-z0-9_]*", left) if t != "_"]
                        if tokens:
                            param_name = tokens[-1]  # npr. "_ name" → "name", "amount" → "amount"
                            if not param_name[0].isupper():  # ne tretiraj Tipove
                                self._declare(param_name, None)
        except Exception:
            # heuristika — ne ruši analizator ako nešto ne očekujemo
            pass

    def exitFuncDecl(self, ctx):
        self._pop()

    # block : '{' stmt* '}' ;
    def enterBlock(self, ctx):
        self._push()

    def exitBlock(self, ctx):
        self._pop()

    # varDecl : (LET | VAR) pattern (':' typeRef)? ( '=' expr )? ';'? ;
    def enterVarDecl(self, ctx):
        # ime varijable (u našem podskupu: IDENT)
        name = None
        if ctx.pattern():
            try:
                name = ctx.pattern().IDENT().getText()
            except Exception:
                name = ctx.pattern().getText()

        if not name:
            return

        # eksplicitni tip (ako postoji)
        typ = ctx.typeRef().getText() if ctx.typeRef() else None

        # infer iz desne strane ako je inicijalizacija:  let x = TypeName(...)
        txt = ctx.getText()
        if "=" in txt:
            try:
                rhs = txt.split("=", 1)[1]
            except Exception:
                rhs = ""
            inferred = self._infer_type_from_ctor(rhs.replace("?.", "."))
            if inferred and not typ:
                typ = inferred

            # provjera izraza inicijalizacije
            self._check_expr_text(rhs, "izrazu dodele")

        # konačno, deklaracija varijable u trenutnom scope-u
        self._declare(name, typ)

    # ifStmt : IF expr block (ELSE (block | ifStmt))? ;
    def enterIfStmt(self, ctx):
        if hasattr(ctx, "expr") and ctx.expr():
            self._check_expr_text(ctx.expr().getText(), "if uslovu")

    # returnStmt : RETURN expr? ';'? ;
    def enterReturnStmt(self, ctx):
        if hasattr(ctx, "expr") and ctx.expr():
            self._check_expr_text(ctx.expr().getText(), "return izrazu")

    # exprStmt : expr ';'? ;
    def enterExprStmt(self, ctx):
        if hasattr(ctx, "expr") and ctx.expr():
            self._check_expr_text(ctx.expr().getText(), "izrazu")
