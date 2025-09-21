# Generated from SwiftParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SwiftParser import SwiftParser
else:
    from SwiftParser import SwiftParser

# This class defines a complete listener for a parse tree produced by SwiftParser.
class SwiftParserListener(ParseTreeListener):

    # Enter a parse tree produced by SwiftParser#program.
    def enterProgram(self, ctx:SwiftParser.ProgramContext):
        pass

    # Exit a parse tree produced by SwiftParser#program.
    def exitProgram(self, ctx:SwiftParser.ProgramContext):
        pass


    # Enter a parse tree produced by SwiftParser#declOrStmt.
    def enterDeclOrStmt(self, ctx:SwiftParser.DeclOrStmtContext):
        pass

    # Exit a parse tree produced by SwiftParser#declOrStmt.
    def exitDeclOrStmt(self, ctx:SwiftParser.DeclOrStmtContext):
        pass


    # Enter a parse tree produced by SwiftParser#importStmt.
    def enterImportStmt(self, ctx:SwiftParser.ImportStmtContext):
        pass

    # Exit a parse tree produced by SwiftParser#importStmt.
    def exitImportStmt(self, ctx:SwiftParser.ImportStmtContext):
        pass


    # Enter a parse tree produced by SwiftParser#classDecl.
    def enterClassDecl(self, ctx:SwiftParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by SwiftParser#classDecl.
    def exitClassDecl(self, ctx:SwiftParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by SwiftParser#extensionDecl.
    def enterExtensionDecl(self, ctx:SwiftParser.ExtensionDeclContext):
        pass

    # Exit a parse tree produced by SwiftParser#extensionDecl.
    def exitExtensionDecl(self, ctx:SwiftParser.ExtensionDeclContext):
        pass


    # Enter a parse tree produced by SwiftParser#member.
    def enterMember(self, ctx:SwiftParser.MemberContext):
        pass

    # Exit a parse tree produced by SwiftParser#member.
    def exitMember(self, ctx:SwiftParser.MemberContext):
        pass


    # Enter a parse tree produced by SwiftParser#funcDecl.
    def enterFuncDecl(self, ctx:SwiftParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by SwiftParser#funcDecl.
    def exitFuncDecl(self, ctx:SwiftParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by SwiftParser#parameterList.
    def enterParameterList(self, ctx:SwiftParser.ParameterListContext):
        pass

    # Exit a parse tree produced by SwiftParser#parameterList.
    def exitParameterList(self, ctx:SwiftParser.ParameterListContext):
        pass


    # Enter a parse tree produced by SwiftParser#parameter.
    def enterParameter(self, ctx:SwiftParser.ParameterContext):
        pass

    # Exit a parse tree produced by SwiftParser#parameter.
    def exitParameter(self, ctx:SwiftParser.ParameterContext):
        pass


    # Enter a parse tree produced by SwiftParser#type.
    def enterType(self, ctx:SwiftParser.TypeContext):
        pass

    # Exit a parse tree produced by SwiftParser#type.
    def exitType(self, ctx:SwiftParser.TypeContext):
        pass


    # Enter a parse tree produced by SwiftParser#emptyStmt.
    def enterEmptyStmt(self, ctx:SwiftParser.EmptyStmtContext):
        pass

    # Exit a parse tree produced by SwiftParser#emptyStmt.
    def exitEmptyStmt(self, ctx:SwiftParser.EmptyStmtContext):
        pass


    # Enter a parse tree produced by SwiftParser#statement.
    def enterStatement(self, ctx:SwiftParser.StatementContext):
        pass

    # Exit a parse tree produced by SwiftParser#statement.
    def exitStatement(self, ctx:SwiftParser.StatementContext):
        pass


    # Enter a parse tree produced by SwiftParser#block.
    def enterBlock(self, ctx:SwiftParser.BlockContext):
        pass

    # Exit a parse tree produced by SwiftParser#block.
    def exitBlock(self, ctx:SwiftParser.BlockContext):
        pass


    # Enter a parse tree produced by SwiftParser#varDecl.
    def enterVarDecl(self, ctx:SwiftParser.VarDeclContext):
        pass

    # Exit a parse tree produced by SwiftParser#varDecl.
    def exitVarDecl(self, ctx:SwiftParser.VarDeclContext):
        pass


    # Enter a parse tree produced by SwiftParser#assignStmt.
    def enterAssignStmt(self, ctx:SwiftParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by SwiftParser#assignStmt.
    def exitAssignStmt(self, ctx:SwiftParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by SwiftParser#returnStmt.
    def enterReturnStmt(self, ctx:SwiftParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by SwiftParser#returnStmt.
    def exitReturnStmt(self, ctx:SwiftParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by SwiftParser#breakStmt.
    def enterBreakStmt(self, ctx:SwiftParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by SwiftParser#breakStmt.
    def exitBreakStmt(self, ctx:SwiftParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by SwiftParser#continueStmt.
    def enterContinueStmt(self, ctx:SwiftParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by SwiftParser#continueStmt.
    def exitContinueStmt(self, ctx:SwiftParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by SwiftParser#throwStmt.
    def enterThrowStmt(self, ctx:SwiftParser.ThrowStmtContext):
        pass

    # Exit a parse tree produced by SwiftParser#throwStmt.
    def exitThrowStmt(self, ctx:SwiftParser.ThrowStmtContext):
        pass


    # Enter a parse tree produced by SwiftParser#ifStmt.
    def enterIfStmt(self, ctx:SwiftParser.IfStmtContext):
        pass

    # Exit a parse tree produced by SwiftParser#ifStmt.
    def exitIfStmt(self, ctx:SwiftParser.IfStmtContext):
        pass


    # Enter a parse tree produced by SwiftParser#whileStmt.
    def enterWhileStmt(self, ctx:SwiftParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by SwiftParser#whileStmt.
    def exitWhileStmt(self, ctx:SwiftParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by SwiftParser#repeatStmt.
    def enterRepeatStmt(self, ctx:SwiftParser.RepeatStmtContext):
        pass

    # Exit a parse tree produced by SwiftParser#repeatStmt.
    def exitRepeatStmt(self, ctx:SwiftParser.RepeatStmtContext):
        pass


    # Enter a parse tree produced by SwiftParser#forInStmt.
    def enterForInStmt(self, ctx:SwiftParser.ForInStmtContext):
        pass

    # Exit a parse tree produced by SwiftParser#forInStmt.
    def exitForInStmt(self, ctx:SwiftParser.ForInStmtContext):
        pass


    # Enter a parse tree produced by SwiftParser#pattern.
    def enterPattern(self, ctx:SwiftParser.PatternContext):
        pass

    # Exit a parse tree produced by SwiftParser#pattern.
    def exitPattern(self, ctx:SwiftParser.PatternContext):
        pass


    # Enter a parse tree produced by SwiftParser#rangeLiteral.
    def enterRangeLiteral(self, ctx:SwiftParser.RangeLiteralContext):
        pass

    # Exit a parse tree produced by SwiftParser#rangeLiteral.
    def exitRangeLiteral(self, ctx:SwiftParser.RangeLiteralContext):
        pass


    # Enter a parse tree produced by SwiftParser#doCatchStmt.
    def enterDoCatchStmt(self, ctx:SwiftParser.DoCatchStmtContext):
        pass

    # Exit a parse tree produced by SwiftParser#doCatchStmt.
    def exitDoCatchStmt(self, ctx:SwiftParser.DoCatchStmtContext):
        pass


    # Enter a parse tree produced by SwiftParser#switchStmt.
    def enterSwitchStmt(self, ctx:SwiftParser.SwitchStmtContext):
        pass

    # Exit a parse tree produced by SwiftParser#switchStmt.
    def exitSwitchStmt(self, ctx:SwiftParser.SwitchStmtContext):
        pass


    # Enter a parse tree produced by SwiftParser#caseClause.
    def enterCaseClause(self, ctx:SwiftParser.CaseClauseContext):
        pass

    # Exit a parse tree produced by SwiftParser#caseClause.
    def exitCaseClause(self, ctx:SwiftParser.CaseClauseContext):
        pass


    # Enter a parse tree produced by SwiftParser#defaultClause.
    def enterDefaultClause(self, ctx:SwiftParser.DefaultClauseContext):
        pass

    # Exit a parse tree produced by SwiftParser#defaultClause.
    def exitDefaultClause(self, ctx:SwiftParser.DefaultClauseContext):
        pass


    # Enter a parse tree produced by SwiftParser#exprStatement.
    def enterExprStatement(self, ctx:SwiftParser.ExprStatementContext):
        pass

    # Exit a parse tree produced by SwiftParser#exprStatement.
    def exitExprStatement(self, ctx:SwiftParser.ExprStatementContext):
        pass


    # Enter a parse tree produced by SwiftParser#tryExpr.
    def enterTryExpr(self, ctx:SwiftParser.TryExprContext):
        pass

    # Exit a parse tree produced by SwiftParser#tryExpr.
    def exitTryExpr(self, ctx:SwiftParser.TryExprContext):
        pass


    # Enter a parse tree produced by SwiftParser#postfixOnly.
    def enterPostfixOnly(self, ctx:SwiftParser.PostfixOnlyContext):
        pass

    # Exit a parse tree produced by SwiftParser#postfixOnly.
    def exitPostfixOnly(self, ctx:SwiftParser.PostfixOnlyContext):
        pass


    # Enter a parse tree produced by SwiftParser#postfixExpr.
    def enterPostfixExpr(self, ctx:SwiftParser.PostfixExprContext):
        pass

    # Exit a parse tree produced by SwiftParser#postfixExpr.
    def exitPostfixExpr(self, ctx:SwiftParser.PostfixExprContext):
        pass


    # Enter a parse tree produced by SwiftParser#postfixSuffix.
    def enterPostfixSuffix(self, ctx:SwiftParser.PostfixSuffixContext):
        pass

    # Exit a parse tree produced by SwiftParser#postfixSuffix.
    def exitPostfixSuffix(self, ctx:SwiftParser.PostfixSuffixContext):
        pass


    # Enter a parse tree produced by SwiftParser#callSuffix.
    def enterCallSuffix(self, ctx:SwiftParser.CallSuffixContext):
        pass

    # Exit a parse tree produced by SwiftParser#callSuffix.
    def exitCallSuffix(self, ctx:SwiftParser.CallSuffixContext):
        pass


    # Enter a parse tree produced by SwiftParser#memberAccess.
    def enterMemberAccess(self, ctx:SwiftParser.MemberAccessContext):
        pass

    # Exit a parse tree produced by SwiftParser#memberAccess.
    def exitMemberAccess(self, ctx:SwiftParser.MemberAccessContext):
        pass


    # Enter a parse tree produced by SwiftParser#argumentList.
    def enterArgumentList(self, ctx:SwiftParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by SwiftParser#argumentList.
    def exitArgumentList(self, ctx:SwiftParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by SwiftParser#primary.
    def enterPrimary(self, ctx:SwiftParser.PrimaryContext):
        pass

    # Exit a parse tree produced by SwiftParser#primary.
    def exitPrimary(self, ctx:SwiftParser.PrimaryContext):
        pass


    # Enter a parse tree produced by SwiftParser#literal.
    def enterLiteral(self, ctx:SwiftParser.LiteralContext):
        pass

    # Exit a parse tree produced by SwiftParser#literal.
    def exitLiteral(self, ctx:SwiftParser.LiteralContext):
        pass



del SwiftParser