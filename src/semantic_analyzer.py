import re
from antlr4 import ParseTreeWalker
from src.antlr_gen.SwiftParserListener import SwiftParserListener  # generiše ga ANTLR

class SemanticAnalyzer(SwiftParserListener):
    def __init__(self):
        self.errors = []
        self._scopes = []             # list[dict[str, dict(type=...)]]
        self._current_type = None
        self._builtins = {"print", "println"}

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
        m = re.match(r"\s*([A-Z][A-Za-z0-9_]*)\s*\(", expr_text)
        return m.group(1) if m else None

    def _member_names_in(self, txt: str):
        return {m.group(1) for m in re.finditer(r"(?:\.|\?\.)\s*([A-Za-z_][A-Za-z0-9_]*)", txt)}

    def _strip_strings(self, txt: str):
        txt = re.sub(r'"(?:\\.|[^"\\])*"', '""', txt)
        txt = re.sub(r"'(?:\\.|[^'\\])*'", "''", txt)
        return txt

    def _check_expr_text(self, txt: str, where: str):
        t = self._strip_strings(txt)

        member_names = self._member_names_in(t)


        arg_labels = {m.group(1) for m in re.finditer(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*:", t)}

        for name in self._ID_RE.findall(t):
            if name in self._builtins or name in {"self", "super", "true", "false", "nil"}:
                continue
            if name and name[0].isupper():
                continue
            if name in member_names:
                continue
            if name in arg_labels:
                continue
            if not self._resolve(name):
                self.errors.append(f"Nedefinisani identifikator '{name}' u {where}")


    def enterTypeDecl(self, ctx):
        self._current_type = ctx.IDENT().getText()

    def exitTypeDecl(self, ctx):
        self._current_type = None

    def enterFuncDecl(self, ctx):
        self._push()
        try:
            pcl = ctx.paramClause()
            if pcl:
                txt = pcl.getText()
                content = txt[1:-1] if txt.startswith("(") and txt.endswith(")") else txt
                for seg in [s.strip() for s in content.split(",") if s.strip()]:
                    parts = seg.split(":")
                    if len(parts) >= 2:
                        left = parts[0].strip()
                        tokens = [t for t in re.findall(r"[A-Za-z_][A-Za-z0-9_]*", left) if t != "_"]
                        if tokens:
                            param_name = tokens[-1] 
                            if not param_name[0].isupper(): 
                                self._declare(param_name, None)
        except Exception:
            pass

    def exitFuncDecl(self, ctx):
        self._pop()

    def enterBlock(self, ctx):
        self._push()

    def exitBlock(self, ctx):
        self._pop()

    # varDecl : (LET | VAR) pattern (':' typeRef)? ( '=' expr )? ';'? ;
    def enterVarDecl(self, ctx):
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
