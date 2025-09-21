# Generated from SwiftParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SwiftParser import SwiftParser
else:
    from SwiftParser import SwiftParser

# This class defines a complete generic visitor for a parse tree produced by SwiftParser.

class SwiftParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SwiftParser#program.
    def visitProgram(self, ctx:SwiftParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#declOrStmt.
    def visitDeclOrStmt(self, ctx:SwiftParser.DeclOrStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#importStmt.
    def visitImportStmt(self, ctx:SwiftParser.ImportStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#classDecl.
    def visitClassDecl(self, ctx:SwiftParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#extensionDecl.
    def visitExtensionDecl(self, ctx:SwiftParser.ExtensionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#member.
    def visitMember(self, ctx:SwiftParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#funcDecl.
    def visitFuncDecl(self, ctx:SwiftParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#parameterList.
    def visitParameterList(self, ctx:SwiftParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#parameter.
    def visitParameter(self, ctx:SwiftParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#type.
    def visitType(self, ctx:SwiftParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#emptyStmt.
    def visitEmptyStmt(self, ctx:SwiftParser.EmptyStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#statement.
    def visitStatement(self, ctx:SwiftParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#block.
    def visitBlock(self, ctx:SwiftParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#varDecl.
    def visitVarDecl(self, ctx:SwiftParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#assignStmt.
    def visitAssignStmt(self, ctx:SwiftParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#returnStmt.
    def visitReturnStmt(self, ctx:SwiftParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#breakStmt.
    def visitBreakStmt(self, ctx:SwiftParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#continueStmt.
    def visitContinueStmt(self, ctx:SwiftParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#throwStmt.
    def visitThrowStmt(self, ctx:SwiftParser.ThrowStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#ifStmt.
    def visitIfStmt(self, ctx:SwiftParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#whileStmt.
    def visitWhileStmt(self, ctx:SwiftParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#repeatStmt.
    def visitRepeatStmt(self, ctx:SwiftParser.RepeatStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#forInStmt.
    def visitForInStmt(self, ctx:SwiftParser.ForInStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#pattern.
    def visitPattern(self, ctx:SwiftParser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#rangeLiteral.
    def visitRangeLiteral(self, ctx:SwiftParser.RangeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#doCatchStmt.
    def visitDoCatchStmt(self, ctx:SwiftParser.DoCatchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#switchStmt.
    def visitSwitchStmt(self, ctx:SwiftParser.SwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#caseClause.
    def visitCaseClause(self, ctx:SwiftParser.CaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#defaultClause.
    def visitDefaultClause(self, ctx:SwiftParser.DefaultClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#exprStatement.
    def visitExprStatement(self, ctx:SwiftParser.ExprStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#tryExpr.
    def visitTryExpr(self, ctx:SwiftParser.TryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#postfixOnly.
    def visitPostfixOnly(self, ctx:SwiftParser.PostfixOnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#postfixExpr.
    def visitPostfixExpr(self, ctx:SwiftParser.PostfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#postfixSuffix.
    def visitPostfixSuffix(self, ctx:SwiftParser.PostfixSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#callSuffix.
    def visitCallSuffix(self, ctx:SwiftParser.CallSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#memberAccess.
    def visitMemberAccess(self, ctx:SwiftParser.MemberAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#argumentList.
    def visitArgumentList(self, ctx:SwiftParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#primary.
    def visitPrimary(self, ctx:SwiftParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#literal.
    def visitLiteral(self, ctx:SwiftParser.LiteralContext):
        return self.visitChildren(ctx)



del SwiftParser