import re
from src.antlr_gen.SwiftParserVisitor import SwiftParserVisitor

class SeqEvent:
    def __init__(self, sender, receiver, message, kind="sync"):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.kind = kind  # "sync" | "create" | "return"

class SeqCollector(SwiftParserVisitor):
    def __init__(self):
        super().__init__()
        self.classes = set()
        self.methods_by_class = {}
        self.known_vars = {}     
        self.current_owner = None    
        self.current_func = None
        self.events = []

    def _sender(self): 
        return self.current_owner or "Global"

    def _add(self, sender, receiver, message, kind="sync"):
        self.events.append(SeqEvent(sender, receiver or "Global", message, kind))

    def _looks_like_type(self, s): 
        return bool(s) and s[0].isupper()

    # ---- typeDecl : (CLASS|STRUCT|ENUM|PROTOCOL|EXTENSION) IDENT typeBody
    def visitTypeDecl(self, ctx):
        name = ctx.IDENT().getText()
        self.classes.add(name)
        self.methods_by_class.setdefault(name, set())

        prev_owner = self.current_owner
        prev_vars  = self.known_vars
        self.current_owner = name
        self.known_vars = {}

        self.visitChildren(ctx)

        self.current_owner = prev_owner
        self.known_vars = prev_vars
        return None

    # ---- funcDecl : FUNC IDENT paramClause returnClause? block
    def visitFuncDecl(self, ctx):
        fname = ctx.IDENT().getText()
        if self.current_owner:
            self.methods_by_class.setdefault(self.current_owner, set()).add(fname)

        prev_func = self.current_func
        prev_vars = self.known_vars
        self.current_func = fname
        self.known_vars = dict(self.known_vars)

        self.visitChildren(ctx)

        self.current_func = prev_func
        self.known_vars = prev_vars
        return None

    # ---- varDecl : (LET|VAR) pattern (':' typeRef)? ('=' expr)? ';'?
    def visitVarDecl(self, ctx):
        name = ctx.pattern().getText()
        # eksplicitni tip?
        if ctx.typeRef():
            self.known_vars[name] = ctx.typeRef().getText()

        # inicijalizacija: detekcija TypeName(...)
        txt = ctx.getText()
        if "=" in txt:
            rhs = txt.split("=", 1)[1]
            rhs_norm = rhs.replace('?.', '.')
            m = re.match(r"\s*([A-Z][A-Za-z0-9_]*)\s*\(", rhs_norm)
            if m:
                tname = m.group(1)
                self.known_vars[name] = tname
                self._add(self._sender(), tname, f"<<create>> {name} = {tname}()", "create")
                return None
        return self.visitChildren(ctx)

    # ---- exprStmt : expr ';'?
    def visitExprStmt(self, ctx):
        txt = ctx.getText()
        if not txt:
            return self.visitChildren(ctx)

        # ukloni 'try', opcionalne lance tretiraj kao '.'
        txt = txt.replace('?.', '.')
        txt = re.sub(r'^\s*try[!?]?(?=[A-Za-z_\(])', '', txt)

        # 1) kreacija:  TypeName(...)
        m_new = re.fullmatch(r"\s*([A-Z][A-Za-z0-9_]*)\s*\([^()]*\)\s*", txt)
        if m_new:
            tname = m_new.group(1)
            self._add(self._sender(), tname, f"<<create>> {tname}()", "create")
            return None

        # 2) member poziv:  recv.method(...)
        m_mem = re.search(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\.\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(", txt)
        if m_mem:
            recv_raw, method = m_mem.group(1), m_mem.group(2)
            if recv_raw in ("self", "Self") and self.current_owner:
                receiver = self.current_owner
            elif recv_raw in self.known_vars:
                receiver = self.known_vars[recv_raw]
            elif self._looks_like_type(recv_raw):
                receiver = recv_raw
            else:
                receiver = recv_raw   # fallback: ime varijable kao participant
            m_full = re.search(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\.\s*([A-Za-z_][A-Za-z0-9_]*)\s*\((.*)\)\s*$", txt)
            if m_full:
                args_text = m_full.group(3).strip()
                label = f"{method}({args_text})"
            else:
                label = method
            self._add(self._sender(), receiver, label)
            return None

        m_call = re.match(r"\s*([A-Za-z_][A-Za-z0-9_]*)\s*\((.*)\)\s*$", txt)
        if m_call:
            callee, args_text = m_call.group(1), m_call.group(2).strip()
            label = f"{callee}({args_text})"
            if self.current_owner and callee in self.methods_by_class.get(self.current_owner, set()):
                self._add(self._sender(), self.current_owner, label)
            else:
                self._add(self._sender(), "Global", label)
            return None

        return self.visitChildren(ctx)
