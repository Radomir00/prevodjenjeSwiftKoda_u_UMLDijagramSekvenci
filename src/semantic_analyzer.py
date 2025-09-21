import re
from antlr4.tree.Tree import ParseTreeWalker
from .antlr_gen.SwiftParserListener import SwiftParserListener

class SemanticAnalyzer(SwiftParserListener):
    def __init__(self):
        self.errors = []
        self._scopes = []            
        self._current_class = None
        self._builtins = {"print"}

    def analyze(self, tree):
        self.errors = []
        self._scopes = [{}]          # global scope
        self._current_class = None
        ParseTreeWalker().walk(self, tree)
        return self.errors

    # --- scope helpers
    def _push(self): self._scopes.append({})
    def _pop(self):
        if self._scopes: self._scopes.pop()
    def _declare(self, name, typ=None):
        s = self._scopes[-1]
        if name in s:
            self.errors.append(f"Dvostruka deklaracija lokalne promjenljive: '{name}'")
        s[name] = {"type": typ}
    def _resolve(self, name):
        for s in reversed(self._scopes):
            if name in s: return s[name]
        return None

    # --- heuristike
    def _infer_type_from_call(self, expr_text: str):
        m = re.match(r"\s*([A-Z][A-Za-z0-9_]*)\s*\(", expr_text)
        return m.group(1) if m else None

    def _member_names_in(self, txt: str):
        return {m.group(1) for m in re.finditer(r"(?:\.|\?\.)\s*([A-Za-z_][A-Za-z0-9_]*)", txt)}

    def _check_expr_text(self, txt: str, where: str):
        txt_wo_strings = re.sub(r'"(?:\\.|[^"\\])*"', '""', txt)
        txt_wo_strings = re.sub(r'\btry(?=[A-Za-z_])', 'try ', txt_wo_strings)
        ids = re.findall(r"[A-Za-z_][A-Za-z0-9_]*", txt_wo_strings)
        member_names = self._member_names_in(txt_wo_strings)

        for name in ids:
            if name in self._builtins or name in {"self", "super", "true", "false", "nil", "try"}:
                continue
            if name[0].isupper():
                continue
            if name in member_names:
                continue
            if not self._resolve(name):
                self.errors.append(f"Nedefinisani identifikator '{name}' u {where}")


    def enterClassDecl(self, ctx): self._current_class = ctx.IDENT().getText()
    def exitClassDecl(self, ctx):  self._current_class = None

    def enterFuncDecl(self, ctx):
        self._push()
        plist = ctx.parameterList()
        if plist:
            for p in plist.parameter():
                name = p.IDENT().getText()
                typ  = p.type_().getText() if p.type_() else None
                self._declare(name, typ)
    def exitFuncDecl(self, ctx): self._pop()

    def enterBlock(self, ctx): self._push()
    def exitBlock(self, ctx):  self._pop()

    def enterVarDecl(self, ctx):
        name = ctx.IDENT().getText()
        typ  = ctx.type_().getText() if ctx.type_() else None
        if not typ and ctx.expression():
            inferred = self._infer_type_from_call(ctx.expression().getText())
            typ = inferred or None
        self._declare(name, typ)
        if ctx.expression():
            self._check_expr_text(ctx.expression().getText(), "izrazu dodele")

    def enterAssignStmt(self, ctx):
        name = ctx.IDENT().getText()
        if not self._resolve(name):
            self.errors.append(f"Nedefinisana promjenljiva u dodeli: '{name}'")
        self._check_expr_text(ctx.expression().getText(), "dodeli")

    def enterReturnStmt(self, ctx):
        if ctx.expression():
            self._check_expr_text(ctx.expression().getText(), "return izrazu")

    def enterThrowStmt(self, ctx):
        self._check_expr_text(ctx.expression().getText(), "throw izrazu")

    def enterIfStmt(self, ctx):
        self._check_expr_text(ctx.expression().getText(), "if uslovu")

    def enterWhileStmt(self, ctx):
        self._check_expr_text(ctx.expression().getText(), "while uslovu")

    def enterRepeatStmt(self, ctx):
        pass

    def enterForInStmt(self, ctx):
        it = ctx.pattern().IDENT().getText()
        self._declare(it, None)

    def enterExprStatement(self, ctx):
        if ctx.expression():
            self._check_expr_text(ctx.expression().getText(), "izrazu")
