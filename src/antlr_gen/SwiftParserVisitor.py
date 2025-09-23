# Generated from grammar/SwiftParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SwiftParser import SwiftParser
else:
    from SwiftParser import SwiftParser

# This class defines a complete generic visitor for a parse tree produced by SwiftParser.

class SwiftParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SwiftParser#compilationUnit.
    def visitCompilationUnit(self, ctx:SwiftParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#topLevelDecl.
    def visitTopLevelDecl(self, ctx:SwiftParser.TopLevelDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#importDecl.
    def visitImportDecl(self, ctx:SwiftParser.ImportDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#importPath.
    def visitImportPath(self, ctx:SwiftParser.ImportPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#typeDecl.
    def visitTypeDecl(self, ctx:SwiftParser.TypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#typeBody.
    def visitTypeBody(self, ctx:SwiftParser.TypeBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#typeMember.
    def visitTypeMember(self, ctx:SwiftParser.TypeMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#funcDecl.
    def visitFuncDecl(self, ctx:SwiftParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#initDecl.
    def visitInitDecl(self, ctx:SwiftParser.InitDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#paramClause.
    def visitParamClause(self, ctx:SwiftParser.ParamClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#paramList.
    def visitParamList(self, ctx:SwiftParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#param.
    def visitParam(self, ctx:SwiftParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#returnClause.
    def visitReturnClause(self, ctx:SwiftParser.ReturnClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#typeRef.
    def visitTypeRef(self, ctx:SwiftParser.TypeRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#typeSuffix.
    def visitTypeSuffix(self, ctx:SwiftParser.TypeSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#varDecl.
    def visitVarDecl(self, ctx:SwiftParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#pattern.
    def visitPattern(self, ctx:SwiftParser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#block.
    def visitBlock(self, ctx:SwiftParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#stmt.
    def visitStmt(self, ctx:SwiftParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#ifStmt.
    def visitIfStmt(self, ctx:SwiftParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#returnStmt.
    def visitReturnStmt(self, ctx:SwiftParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#exprStmt.
    def visitExprStmt(self, ctx:SwiftParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#expr.
    def visitExpr(self, ctx:SwiftParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#assignExpr.
    def visitAssignExpr(self, ctx:SwiftParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#conditionalExpr.
    def visitConditionalExpr(self, ctx:SwiftParser.ConditionalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#logicalOrExpr.
    def visitLogicalOrExpr(self, ctx:SwiftParser.LogicalOrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#logicalAndExpr.
    def visitLogicalAndExpr(self, ctx:SwiftParser.LogicalAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#equalityExpr.
    def visitEqualityExpr(self, ctx:SwiftParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#relationalExpr.
    def visitRelationalExpr(self, ctx:SwiftParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:SwiftParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:SwiftParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#unaryExpr.
    def visitUnaryExpr(self, ctx:SwiftParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#postfixExpr.
    def visitPostfixExpr(self, ctx:SwiftParser.PostfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#postfixOp.
    def visitPostfixOp(self, ctx:SwiftParser.PostfixOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#memberAccess.
    def visitMemberAccess(self, ctx:SwiftParser.MemberAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#optionalChain.
    def visitOptionalChain(self, ctx:SwiftParser.OptionalChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#callSuffix.
    def visitCallSuffix(self, ctx:SwiftParser.CallSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#argList.
    def visitArgList(self, ctx:SwiftParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#arg.
    def visitArg(self, ctx:SwiftParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:SwiftParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#collectionLiteral.
    def visitCollectionLiteral(self, ctx:SwiftParser.CollectionLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SwiftParser#literal.
    def visitLiteral(self, ctx:SwiftParser.LiteralContext):
        return self.visitChildren(ctx)



del SwiftParser