# Generated from grammar/SwiftParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SwiftParser import SwiftParser
else:
    from SwiftParser import SwiftParser

# This class defines a complete listener for a parse tree produced by SwiftParser.
class SwiftParserListener(ParseTreeListener):

    # Enter a parse tree produced by SwiftParser#compilationUnit.
    def enterCompilationUnit(self, ctx:SwiftParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by SwiftParser#compilationUnit.
    def exitCompilationUnit(self, ctx:SwiftParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by SwiftParser#topLevelDecl.
    def enterTopLevelDecl(self, ctx:SwiftParser.TopLevelDeclContext):
        pass

    # Exit a parse tree produced by SwiftParser#topLevelDecl.
    def exitTopLevelDecl(self, ctx:SwiftParser.TopLevelDeclContext):
        pass


    # Enter a parse tree produced by SwiftParser#importDecl.
    def enterImportDecl(self, ctx:SwiftParser.ImportDeclContext):
        pass

    # Exit a parse tree produced by SwiftParser#importDecl.
    def exitImportDecl(self, ctx:SwiftParser.ImportDeclContext):
        pass


    # Enter a parse tree produced by SwiftParser#importPath.
    def enterImportPath(self, ctx:SwiftParser.ImportPathContext):
        pass

    # Exit a parse tree produced by SwiftParser#importPath.
    def exitImportPath(self, ctx:SwiftParser.ImportPathContext):
        pass


    # Enter a parse tree produced by SwiftParser#typeDecl.
    def enterTypeDecl(self, ctx:SwiftParser.TypeDeclContext):
        pass

    # Exit a parse tree produced by SwiftParser#typeDecl.
    def exitTypeDecl(self, ctx:SwiftParser.TypeDeclContext):
        pass


    # Enter a parse tree produced by SwiftParser#typeBody.
    def enterTypeBody(self, ctx:SwiftParser.TypeBodyContext):
        pass

    # Exit a parse tree produced by SwiftParser#typeBody.
    def exitTypeBody(self, ctx:SwiftParser.TypeBodyContext):
        pass


    # Enter a parse tree produced by SwiftParser#typeMember.
    def enterTypeMember(self, ctx:SwiftParser.TypeMemberContext):
        pass

    # Exit a parse tree produced by SwiftParser#typeMember.
    def exitTypeMember(self, ctx:SwiftParser.TypeMemberContext):
        pass


    # Enter a parse tree produced by SwiftParser#funcDecl.
    def enterFuncDecl(self, ctx:SwiftParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by SwiftParser#funcDecl.
    def exitFuncDecl(self, ctx:SwiftParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by SwiftParser#initDecl.
    def enterInitDecl(self, ctx:SwiftParser.InitDeclContext):
        pass

    # Exit a parse tree produced by SwiftParser#initDecl.
    def exitInitDecl(self, ctx:SwiftParser.InitDeclContext):
        pass


    # Enter a parse tree produced by SwiftParser#paramClause.
    def enterParamClause(self, ctx:SwiftParser.ParamClauseContext):
        pass

    # Exit a parse tree produced by SwiftParser#paramClause.
    def exitParamClause(self, ctx:SwiftParser.ParamClauseContext):
        pass


    # Enter a parse tree produced by SwiftParser#paramList.
    def enterParamList(self, ctx:SwiftParser.ParamListContext):
        pass

    # Exit a parse tree produced by SwiftParser#paramList.
    def exitParamList(self, ctx:SwiftParser.ParamListContext):
        pass


    # Enter a parse tree produced by SwiftParser#param.
    def enterParam(self, ctx:SwiftParser.ParamContext):
        pass

    # Exit a parse tree produced by SwiftParser#param.
    def exitParam(self, ctx:SwiftParser.ParamContext):
        pass


    # Enter a parse tree produced by SwiftParser#returnClause.
    def enterReturnClause(self, ctx:SwiftParser.ReturnClauseContext):
        pass

    # Exit a parse tree produced by SwiftParser#returnClause.
    def exitReturnClause(self, ctx:SwiftParser.ReturnClauseContext):
        pass


    # Enter a parse tree produced by SwiftParser#typeRef.
    def enterTypeRef(self, ctx:SwiftParser.TypeRefContext):
        pass

    # Exit a parse tree produced by SwiftParser#typeRef.
    def exitTypeRef(self, ctx:SwiftParser.TypeRefContext):
        pass


    # Enter a parse tree produced by SwiftParser#typeSuffix.
    def enterTypeSuffix(self, ctx:SwiftParser.TypeSuffixContext):
        pass

    # Exit a parse tree produced by SwiftParser#typeSuffix.
    def exitTypeSuffix(self, ctx:SwiftParser.TypeSuffixContext):
        pass


    # Enter a parse tree produced by SwiftParser#varDecl.
    def enterVarDecl(self, ctx:SwiftParser.VarDeclContext):
        pass

    # Exit a parse tree produced by SwiftParser#varDecl.
    def exitVarDecl(self, ctx:SwiftParser.VarDeclContext):
        pass


    # Enter a parse tree produced by SwiftParser#pattern.
    def enterPattern(self, ctx:SwiftParser.PatternContext):
        pass

    # Exit a parse tree produced by SwiftParser#pattern.
    def exitPattern(self, ctx:SwiftParser.PatternContext):
        pass


    # Enter a parse tree produced by SwiftParser#block.
    def enterBlock(self, ctx:SwiftParser.BlockContext):
        pass

    # Exit a parse tree produced by SwiftParser#block.
    def exitBlock(self, ctx:SwiftParser.BlockContext):
        pass


    # Enter a parse tree produced by SwiftParser#stmt.
    def enterStmt(self, ctx:SwiftParser.StmtContext):
        pass

    # Exit a parse tree produced by SwiftParser#stmt.
    def exitStmt(self, ctx:SwiftParser.StmtContext):
        pass


    # Enter a parse tree produced by SwiftParser#ifStmt.
    def enterIfStmt(self, ctx:SwiftParser.IfStmtContext):
        pass

    # Exit a parse tree produced by SwiftParser#ifStmt.
    def exitIfStmt(self, ctx:SwiftParser.IfStmtContext):
        pass


    # Enter a parse tree produced by SwiftParser#returnStmt.
    def enterReturnStmt(self, ctx:SwiftParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by SwiftParser#returnStmt.
    def exitReturnStmt(self, ctx:SwiftParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by SwiftParser#exprStmt.
    def enterExprStmt(self, ctx:SwiftParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by SwiftParser#exprStmt.
    def exitExprStmt(self, ctx:SwiftParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by SwiftParser#expr.
    def enterExpr(self, ctx:SwiftParser.ExprContext):
        pass

    # Exit a parse tree produced by SwiftParser#expr.
    def exitExpr(self, ctx:SwiftParser.ExprContext):
        pass


    # Enter a parse tree produced by SwiftParser#assignExpr.
    def enterAssignExpr(self, ctx:SwiftParser.AssignExprContext):
        pass

    # Exit a parse tree produced by SwiftParser#assignExpr.
    def exitAssignExpr(self, ctx:SwiftParser.AssignExprContext):
        pass


    # Enter a parse tree produced by SwiftParser#conditionalExpr.
    def enterConditionalExpr(self, ctx:SwiftParser.ConditionalExprContext):
        pass

    # Exit a parse tree produced by SwiftParser#conditionalExpr.
    def exitConditionalExpr(self, ctx:SwiftParser.ConditionalExprContext):
        pass


    # Enter a parse tree produced by SwiftParser#logicalOrExpr.
    def enterLogicalOrExpr(self, ctx:SwiftParser.LogicalOrExprContext):
        pass

    # Exit a parse tree produced by SwiftParser#logicalOrExpr.
    def exitLogicalOrExpr(self, ctx:SwiftParser.LogicalOrExprContext):
        pass


    # Enter a parse tree produced by SwiftParser#logicalAndExpr.
    def enterLogicalAndExpr(self, ctx:SwiftParser.LogicalAndExprContext):
        pass

    # Exit a parse tree produced by SwiftParser#logicalAndExpr.
    def exitLogicalAndExpr(self, ctx:SwiftParser.LogicalAndExprContext):
        pass


    # Enter a parse tree produced by SwiftParser#equalityExpr.
    def enterEqualityExpr(self, ctx:SwiftParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by SwiftParser#equalityExpr.
    def exitEqualityExpr(self, ctx:SwiftParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by SwiftParser#relationalExpr.
    def enterRelationalExpr(self, ctx:SwiftParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by SwiftParser#relationalExpr.
    def exitRelationalExpr(self, ctx:SwiftParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by SwiftParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:SwiftParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by SwiftParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:SwiftParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by SwiftParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:SwiftParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by SwiftParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:SwiftParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by SwiftParser#unaryExpr.
    def enterUnaryExpr(self, ctx:SwiftParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by SwiftParser#unaryExpr.
    def exitUnaryExpr(self, ctx:SwiftParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by SwiftParser#postfixExpr.
    def enterPostfixExpr(self, ctx:SwiftParser.PostfixExprContext):
        pass

    # Exit a parse tree produced by SwiftParser#postfixExpr.
    def exitPostfixExpr(self, ctx:SwiftParser.PostfixExprContext):
        pass


    # Enter a parse tree produced by SwiftParser#postfixOp.
    def enterPostfixOp(self, ctx:SwiftParser.PostfixOpContext):
        pass

    # Exit a parse tree produced by SwiftParser#postfixOp.
    def exitPostfixOp(self, ctx:SwiftParser.PostfixOpContext):
        pass


    # Enter a parse tree produced by SwiftParser#memberAccess.
    def enterMemberAccess(self, ctx:SwiftParser.MemberAccessContext):
        pass

    # Exit a parse tree produced by SwiftParser#memberAccess.
    def exitMemberAccess(self, ctx:SwiftParser.MemberAccessContext):
        pass


    # Enter a parse tree produced by SwiftParser#optionalChain.
    def enterOptionalChain(self, ctx:SwiftParser.OptionalChainContext):
        pass

    # Exit a parse tree produced by SwiftParser#optionalChain.
    def exitOptionalChain(self, ctx:SwiftParser.OptionalChainContext):
        pass


    # Enter a parse tree produced by SwiftParser#callSuffix.
    def enterCallSuffix(self, ctx:SwiftParser.CallSuffixContext):
        pass

    # Exit a parse tree produced by SwiftParser#callSuffix.
    def exitCallSuffix(self, ctx:SwiftParser.CallSuffixContext):
        pass


    # Enter a parse tree produced by SwiftParser#argList.
    def enterArgList(self, ctx:SwiftParser.ArgListContext):
        pass

    # Exit a parse tree produced by SwiftParser#argList.
    def exitArgList(self, ctx:SwiftParser.ArgListContext):
        pass


    # Enter a parse tree produced by SwiftParser#arg.
    def enterArg(self, ctx:SwiftParser.ArgContext):
        pass

    # Exit a parse tree produced by SwiftParser#arg.
    def exitArg(self, ctx:SwiftParser.ArgContext):
        pass


    # Enter a parse tree produced by SwiftParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:SwiftParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by SwiftParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:SwiftParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by SwiftParser#collectionLiteral.
    def enterCollectionLiteral(self, ctx:SwiftParser.CollectionLiteralContext):
        pass

    # Exit a parse tree produced by SwiftParser#collectionLiteral.
    def exitCollectionLiteral(self, ctx:SwiftParser.CollectionLiteralContext):
        pass


    # Enter a parse tree produced by SwiftParser#literal.
    def enterLiteral(self, ctx:SwiftParser.LiteralContext):
        pass

    # Exit a parse tree produced by SwiftParser#literal.
    def exitLiteral(self, ctx:SwiftParser.LiteralContext):
        pass



del SwiftParser