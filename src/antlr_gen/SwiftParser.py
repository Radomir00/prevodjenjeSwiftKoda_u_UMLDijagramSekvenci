# Generated from grammar/SwiftParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,74,366,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,1,0,5,0,86,8,0,10,0,12,0,89,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,3,1,98,8,1,1,2,1,2,1,2,1,3,1,3,1,3,5,3,106,8,3,10,
        3,12,3,109,9,3,1,4,1,4,1,4,1,4,1,5,1,5,5,5,117,8,5,10,5,12,5,120,
        9,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,128,8,6,1,7,1,7,1,7,1,7,3,7,134,
        8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,3,9,144,8,9,1,9,1,9,1,10,1,10,
        1,10,5,10,151,8,10,10,10,12,10,154,9,10,1,11,1,11,3,11,158,8,11,
        1,11,1,11,1,11,3,11,163,8,11,1,12,1,12,1,12,1,13,1,13,1,13,5,13,
        171,8,13,10,13,12,13,174,9,13,1,13,5,13,177,8,13,10,13,12,13,180,
        9,13,1,14,1,14,1,14,3,14,185,8,14,1,15,1,15,1,15,1,15,3,15,191,8,
        15,1,15,1,15,3,15,195,8,15,1,15,3,15,198,8,15,1,16,1,16,1,17,1,17,
        5,17,204,8,17,10,17,12,17,207,9,17,1,17,1,17,1,18,1,18,1,18,1,18,
        1,18,3,18,216,8,18,1,19,1,19,1,19,1,19,1,19,1,19,3,19,224,8,19,3,
        19,226,8,19,1,20,1,20,3,20,230,8,20,1,20,3,20,233,8,20,1,21,1,21,
        3,21,237,8,21,1,22,1,22,1,23,1,23,1,23,3,23,244,8,23,1,24,1,24,1,
        25,1,25,1,25,5,25,251,8,25,10,25,12,25,254,9,25,1,26,1,26,1,26,5,
        26,259,8,26,10,26,12,26,262,9,26,1,27,1,27,1,27,5,27,267,8,27,10,
        27,12,27,270,9,27,1,28,1,28,1,28,5,28,275,8,28,10,28,12,28,278,9,
        28,1,29,1,29,1,29,5,29,283,8,29,10,29,12,29,286,9,29,1,30,1,30,1,
        30,5,30,291,8,30,10,30,12,30,294,9,30,1,31,3,31,297,8,31,1,31,1,
        31,1,32,1,32,5,32,303,8,32,10,32,12,32,306,9,32,1,33,1,33,1,33,3,
        33,311,8,33,1,34,1,34,1,34,1,35,1,35,3,35,318,8,35,1,36,1,36,3,36,
        322,8,36,1,36,1,36,1,37,1,37,1,37,5,37,329,8,37,10,37,12,37,332,
        9,37,1,38,1,38,3,38,336,8,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,
        1,39,1,39,1,39,1,39,3,39,349,8,39,1,40,1,40,1,40,1,40,5,40,355,8,
        40,10,40,12,40,358,9,40,3,40,360,8,40,1,40,1,40,1,41,1,41,1,41,0,
        0,42,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,0,8,
        1,0,1,5,1,0,10,11,1,0,40,41,2,0,38,39,50,51,1,0,45,46,1,0,47,49,
        2,0,45,46,52,52,2,0,31,33,68,70,376,0,87,1,0,0,0,2,97,1,0,0,0,4,
        99,1,0,0,0,6,102,1,0,0,0,8,110,1,0,0,0,10,114,1,0,0,0,12,127,1,0,
        0,0,14,129,1,0,0,0,16,137,1,0,0,0,18,141,1,0,0,0,20,147,1,0,0,0,
        22,157,1,0,0,0,24,164,1,0,0,0,26,167,1,0,0,0,28,184,1,0,0,0,30,186,
        1,0,0,0,32,199,1,0,0,0,34,201,1,0,0,0,36,215,1,0,0,0,38,217,1,0,
        0,0,40,227,1,0,0,0,42,234,1,0,0,0,44,238,1,0,0,0,46,240,1,0,0,0,
        48,245,1,0,0,0,50,247,1,0,0,0,52,255,1,0,0,0,54,263,1,0,0,0,56,271,
        1,0,0,0,58,279,1,0,0,0,60,287,1,0,0,0,62,296,1,0,0,0,64,300,1,0,
        0,0,66,310,1,0,0,0,68,312,1,0,0,0,70,315,1,0,0,0,72,319,1,0,0,0,
        74,325,1,0,0,0,76,335,1,0,0,0,78,348,1,0,0,0,80,350,1,0,0,0,82,363,
        1,0,0,0,84,86,3,2,1,0,85,84,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,
        87,88,1,0,0,0,88,90,1,0,0,0,89,87,1,0,0,0,90,91,5,0,0,1,91,1,1,0,
        0,0,92,98,3,4,2,0,93,98,3,8,4,0,94,98,3,14,7,0,95,98,3,30,15,0,96,
        98,3,36,18,0,97,92,1,0,0,0,97,93,1,0,0,0,97,94,1,0,0,0,97,95,1,0,
        0,0,97,96,1,0,0,0,98,3,1,0,0,0,99,100,5,28,0,0,100,101,3,6,3,0,101,
        5,1,0,0,0,102,107,5,71,0,0,103,104,5,57,0,0,104,106,5,71,0,0,105,
        103,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,
        7,1,0,0,0,109,107,1,0,0,0,110,111,7,0,0,0,111,112,5,71,0,0,112,113,
        3,10,5,0,113,9,1,0,0,0,114,118,5,64,0,0,115,117,3,12,6,0,116,115,
        1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,121,
        1,0,0,0,120,118,1,0,0,0,121,122,5,65,0,0,122,11,1,0,0,0,123,128,
        3,14,7,0,124,128,3,16,8,0,125,128,3,30,15,0,126,128,3,36,18,0,127,
        123,1,0,0,0,127,124,1,0,0,0,127,125,1,0,0,0,127,126,1,0,0,0,128,
        13,1,0,0,0,129,130,5,6,0,0,130,131,5,71,0,0,131,133,3,18,9,0,132,
        134,3,24,12,0,133,132,1,0,0,0,133,134,1,0,0,0,134,135,1,0,0,0,135,
        136,3,34,17,0,136,15,1,0,0,0,137,138,5,7,0,0,138,139,3,18,9,0,139,
        140,3,34,17,0,140,17,1,0,0,0,141,143,5,62,0,0,142,144,3,20,10,0,
        143,142,1,0,0,0,143,144,1,0,0,0,144,145,1,0,0,0,145,146,5,63,0,0,
        146,19,1,0,0,0,147,152,3,22,11,0,148,149,5,56,0,0,149,151,3,22,11,
        0,150,148,1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,
        0,153,21,1,0,0,0,154,152,1,0,0,0,155,156,5,71,0,0,156,158,5,54,0,
        0,157,155,1,0,0,0,157,158,1,0,0,0,158,159,1,0,0,0,159,162,3,26,13,
        0,160,161,5,44,0,0,161,163,3,44,22,0,162,160,1,0,0,0,162,163,1,0,
        0,0,163,23,1,0,0,0,164,165,5,37,0,0,165,166,3,26,13,0,166,25,1,0,
        0,0,167,172,5,71,0,0,168,169,5,57,0,0,169,171,5,71,0,0,170,168,1,
        0,0,0,171,174,1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,178,1,
        0,0,0,174,172,1,0,0,0,175,177,3,28,14,0,176,175,1,0,0,0,177,180,
        1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,27,1,0,0,0,180,178,1,
        0,0,0,181,185,5,53,0,0,182,183,5,66,0,0,183,185,5,67,0,0,184,181,
        1,0,0,0,184,182,1,0,0,0,185,29,1,0,0,0,186,187,7,1,0,0,187,190,3,
        32,16,0,188,189,5,54,0,0,189,191,3,26,13,0,190,188,1,0,0,0,190,191,
        1,0,0,0,191,194,1,0,0,0,192,193,5,44,0,0,193,195,3,44,22,0,194,192,
        1,0,0,0,194,195,1,0,0,0,195,197,1,0,0,0,196,198,5,55,0,0,197,196,
        1,0,0,0,197,198,1,0,0,0,198,31,1,0,0,0,199,200,5,71,0,0,200,33,1,
        0,0,0,201,205,5,64,0,0,202,204,3,36,18,0,203,202,1,0,0,0,204,207,
        1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,208,1,0,0,0,207,205,
        1,0,0,0,208,209,5,65,0,0,209,35,1,0,0,0,210,216,3,38,19,0,211,216,
        3,40,20,0,212,216,3,42,21,0,213,216,3,30,15,0,214,216,3,34,17,0,
        215,210,1,0,0,0,215,211,1,0,0,0,215,212,1,0,0,0,215,213,1,0,0,0,
        215,214,1,0,0,0,216,37,1,0,0,0,217,218,5,17,0,0,218,219,3,44,22,
        0,219,225,3,34,17,0,220,223,5,18,0,0,221,224,3,34,17,0,222,224,3,
        38,19,0,223,221,1,0,0,0,223,222,1,0,0,0,224,226,1,0,0,0,225,220,
        1,0,0,0,225,226,1,0,0,0,226,39,1,0,0,0,227,229,5,12,0,0,228,230,
        3,44,22,0,229,228,1,0,0,0,229,230,1,0,0,0,230,232,1,0,0,0,231,233,
        5,55,0,0,232,231,1,0,0,0,232,233,1,0,0,0,233,41,1,0,0,0,234,236,
        3,44,22,0,235,237,5,55,0,0,236,235,1,0,0,0,236,237,1,0,0,0,237,43,
        1,0,0,0,238,239,3,46,23,0,239,45,1,0,0,0,240,243,3,48,24,0,241,242,
        5,44,0,0,242,244,3,46,23,0,243,241,1,0,0,0,243,244,1,0,0,0,244,47,
        1,0,0,0,245,246,3,50,25,0,246,49,1,0,0,0,247,252,3,52,26,0,248,249,
        5,43,0,0,249,251,3,52,26,0,250,248,1,0,0,0,251,254,1,0,0,0,252,250,
        1,0,0,0,252,253,1,0,0,0,253,51,1,0,0,0,254,252,1,0,0,0,255,260,3,
        54,27,0,256,257,5,42,0,0,257,259,3,54,27,0,258,256,1,0,0,0,259,262,
        1,0,0,0,260,258,1,0,0,0,260,261,1,0,0,0,261,53,1,0,0,0,262,260,1,
        0,0,0,263,268,3,56,28,0,264,265,7,2,0,0,265,267,3,56,28,0,266,264,
        1,0,0,0,267,270,1,0,0,0,268,266,1,0,0,0,268,269,1,0,0,0,269,55,1,
        0,0,0,270,268,1,0,0,0,271,276,3,58,29,0,272,273,7,3,0,0,273,275,
        3,58,29,0,274,272,1,0,0,0,275,278,1,0,0,0,276,274,1,0,0,0,276,277,
        1,0,0,0,277,57,1,0,0,0,278,276,1,0,0,0,279,284,3,60,30,0,280,281,
        7,4,0,0,281,283,3,60,30,0,282,280,1,0,0,0,283,286,1,0,0,0,284,282,
        1,0,0,0,284,285,1,0,0,0,285,59,1,0,0,0,286,284,1,0,0,0,287,292,3,
        62,31,0,288,289,7,5,0,0,289,291,3,62,31,0,290,288,1,0,0,0,291,294,
        1,0,0,0,292,290,1,0,0,0,292,293,1,0,0,0,293,61,1,0,0,0,294,292,1,
        0,0,0,295,297,7,6,0,0,296,295,1,0,0,0,296,297,1,0,0,0,297,298,1,
        0,0,0,298,299,3,64,32,0,299,63,1,0,0,0,300,304,3,78,39,0,301,303,
        3,66,33,0,302,301,1,0,0,0,303,306,1,0,0,0,304,302,1,0,0,0,304,305,
        1,0,0,0,305,65,1,0,0,0,306,304,1,0,0,0,307,311,3,68,34,0,308,311,
        3,72,36,0,309,311,3,70,35,0,310,307,1,0,0,0,310,308,1,0,0,0,310,
        309,1,0,0,0,311,67,1,0,0,0,312,313,5,57,0,0,313,314,5,71,0,0,314,
        69,1,0,0,0,315,317,5,34,0,0,316,318,5,71,0,0,317,316,1,0,0,0,317,
        318,1,0,0,0,318,71,1,0,0,0,319,321,5,62,0,0,320,322,3,74,37,0,321,
        320,1,0,0,0,321,322,1,0,0,0,322,323,1,0,0,0,323,324,5,63,0,0,324,
        73,1,0,0,0,325,330,3,76,38,0,326,327,5,56,0,0,327,329,3,76,38,0,
        328,326,1,0,0,0,329,332,1,0,0,0,330,328,1,0,0,0,330,331,1,0,0,0,
        331,75,1,0,0,0,332,330,1,0,0,0,333,334,5,71,0,0,334,336,5,54,0,0,
        335,333,1,0,0,0,335,336,1,0,0,0,336,337,1,0,0,0,337,338,3,44,22,
        0,338,77,1,0,0,0,339,349,3,82,41,0,340,349,5,29,0,0,341,349,5,30,
        0,0,342,349,5,71,0,0,343,344,5,62,0,0,344,345,3,44,22,0,345,346,
        5,63,0,0,346,349,1,0,0,0,347,349,3,80,40,0,348,339,1,0,0,0,348,340,
        1,0,0,0,348,341,1,0,0,0,348,342,1,0,0,0,348,343,1,0,0,0,348,347,
        1,0,0,0,349,79,1,0,0,0,350,359,5,66,0,0,351,356,3,44,22,0,352,353,
        5,56,0,0,353,355,3,44,22,0,354,352,1,0,0,0,355,358,1,0,0,0,356,354,
        1,0,0,0,356,357,1,0,0,0,357,360,1,0,0,0,358,356,1,0,0,0,359,351,
        1,0,0,0,359,360,1,0,0,0,360,361,1,0,0,0,361,362,5,67,0,0,362,81,
        1,0,0,0,363,364,7,7,0,0,364,83,1,0,0,0,40,87,97,107,118,127,133,
        143,152,157,162,172,178,184,190,194,197,205,215,223,225,229,232,
        236,243,252,260,268,276,284,292,296,304,310,317,321,330,335,348,
        356,359
    ]

class SwiftParser ( Parser ):

    grammarFileName = "SwiftParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'struct'", "'enum'", "'extension'", 
                     "'protocol'", "'func'", "'init'", "'deinit'", "'static'", 
                     "'let'", "'var'", "'return'", "'break'", "'continue'", 
                     "'throw'", "'try'", "'if'", "'else'", "'for'", "'while'", 
                     "'repeat'", "'do'", "'switch'", "'case'", "'default'", 
                     "'guard'", "'where'", "'import'", "'self'", "'super'", 
                     "'true'", "'false'", "'nil'", "'?.'", "'...'", "'..<'", 
                     "'->'", "'<='", "'>='", "'=='", "'!='", "'&&'", "'||'", 
                     "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'<'", "'>'", 
                     "'!'", "'?'", "':'", "';'", "','", "'.'", "'@'", "'&'", 
                     "'|'", "'#'", "'('", "')'", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "STRUCT", "ENUM", "EXTENSION", 
                      "PROTOCOL", "FUNC", "INIT", "DEINIT", "STATIC", "LET", 
                      "VAR", "RETURN", "BREAK", "CONTINUE", "THROW", "TRY", 
                      "IF", "ELSE", "FOR", "WHILE", "REPEAT", "DO", "SWITCH", 
                      "CASE", "DEFAULT", "GUARD", "WHERE", "IMPORT", "SELF", 
                      "SUPER", "TRUE", "FALSE", "NIL", "OPTIONAL_CHAIN", 
                      "RANGE_CLOSED", "RANGE_HALF", "ARROW", "LE", "GE", 
                      "EQ", "NEQ", "AND_AND", "OR_OR", "ASSIGN", "PLUS", 
                      "MINUS", "STAR", "DIV", "MOD", "LT", "GT", "NOT", 
                      "QUESTION", "COLON", "SEMI", "COMMA", "DOT", "AT", 
                      "AMP", "PIPE", "AROB", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "LBRACK", "RBRACK", "FLOAT", "INT", "STRING", 
                      "IDENT", "LINE_COMMENT", "BLOCK_COMMENT", "WS" ]

    RULE_compilationUnit = 0
    RULE_topLevelDecl = 1
    RULE_importDecl = 2
    RULE_importPath = 3
    RULE_typeDecl = 4
    RULE_typeBody = 5
    RULE_typeMember = 6
    RULE_funcDecl = 7
    RULE_initDecl = 8
    RULE_paramClause = 9
    RULE_paramList = 10
    RULE_param = 11
    RULE_returnClause = 12
    RULE_typeRef = 13
    RULE_typeSuffix = 14
    RULE_varDecl = 15
    RULE_pattern = 16
    RULE_block = 17
    RULE_stmt = 18
    RULE_ifStmt = 19
    RULE_returnStmt = 20
    RULE_exprStmt = 21
    RULE_expr = 22
    RULE_assignExpr = 23
    RULE_conditionalExpr = 24
    RULE_logicalOrExpr = 25
    RULE_logicalAndExpr = 26
    RULE_equalityExpr = 27
    RULE_relationalExpr = 28
    RULE_additiveExpr = 29
    RULE_multiplicativeExpr = 30
    RULE_unaryExpr = 31
    RULE_postfixExpr = 32
    RULE_postfixOp = 33
    RULE_memberAccess = 34
    RULE_optionalChain = 35
    RULE_callSuffix = 36
    RULE_argList = 37
    RULE_arg = 38
    RULE_primaryExpr = 39
    RULE_collectionLiteral = 40
    RULE_literal = 41

    ruleNames =  [ "compilationUnit", "topLevelDecl", "importDecl", "importPath", 
                   "typeDecl", "typeBody", "typeMember", "funcDecl", "initDecl", 
                   "paramClause", "paramList", "param", "returnClause", 
                   "typeRef", "typeSuffix", "varDecl", "pattern", "block", 
                   "stmt", "ifStmt", "returnStmt", "exprStmt", "expr", "assignExpr", 
                   "conditionalExpr", "logicalOrExpr", "logicalAndExpr", 
                   "equalityExpr", "relationalExpr", "additiveExpr", "multiplicativeExpr", 
                   "unaryExpr", "postfixExpr", "postfixOp", "memberAccess", 
                   "optionalChain", "callSuffix", "argList", "arg", "primaryExpr", 
                   "collectionLiteral", "literal" ]

    EOF = Token.EOF
    CLASS=1
    STRUCT=2
    ENUM=3
    EXTENSION=4
    PROTOCOL=5
    FUNC=6
    INIT=7
    DEINIT=8
    STATIC=9
    LET=10
    VAR=11
    RETURN=12
    BREAK=13
    CONTINUE=14
    THROW=15
    TRY=16
    IF=17
    ELSE=18
    FOR=19
    WHILE=20
    REPEAT=21
    DO=22
    SWITCH=23
    CASE=24
    DEFAULT=25
    GUARD=26
    WHERE=27
    IMPORT=28
    SELF=29
    SUPER=30
    TRUE=31
    FALSE=32
    NIL=33
    OPTIONAL_CHAIN=34
    RANGE_CLOSED=35
    RANGE_HALF=36
    ARROW=37
    LE=38
    GE=39
    EQ=40
    NEQ=41
    AND_AND=42
    OR_OR=43
    ASSIGN=44
    PLUS=45
    MINUS=46
    STAR=47
    DIV=48
    MOD=49
    LT=50
    GT=51
    NOT=52
    QUESTION=53
    COLON=54
    SEMI=55
    COMMA=56
    DOT=57
    AT=58
    AMP=59
    PIPE=60
    AROB=61
    LPAREN=62
    RPAREN=63
    LBRACE=64
    RBRACE=65
    LBRACK=66
    RBRACK=67
    FLOAT=68
    INT=69
    STRING=70
    IDENT=71
    LINE_COMMENT=72
    BLOCK_COMMENT=73
    WS=74

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompilationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SwiftParser.EOF, 0)

        def topLevelDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwiftParser.TopLevelDeclContext)
            else:
                return self.getTypedRuleContext(SwiftParser.TopLevelDeclContext,i)


        def getRuleIndex(self):
            return SwiftParser.RULE_compilationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilationUnit" ):
                listener.enterCompilationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilationUnit" ):
                listener.exitCompilationUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompilationUnit" ):
                return visitor.visitCompilationUnit(self)
            else:
                return visitor.visitChildren(self)




    def compilationUnit(self):

        localctx = SwiftParser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compilationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4616295188082596990) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 245) != 0):
                self.state = 84
                self.topLevelDecl()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(SwiftParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopLevelDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def importDecl(self):
            return self.getTypedRuleContext(SwiftParser.ImportDeclContext,0)


        def typeDecl(self):
            return self.getTypedRuleContext(SwiftParser.TypeDeclContext,0)


        def funcDecl(self):
            return self.getTypedRuleContext(SwiftParser.FuncDeclContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(SwiftParser.VarDeclContext,0)


        def stmt(self):
            return self.getTypedRuleContext(SwiftParser.StmtContext,0)


        def getRuleIndex(self):
            return SwiftParser.RULE_topLevelDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopLevelDecl" ):
                listener.enterTopLevelDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopLevelDecl" ):
                listener.exitTopLevelDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopLevelDecl" ):
                return visitor.visitTopLevelDecl(self)
            else:
                return visitor.visitChildren(self)




    def topLevelDecl(self):

        localctx = SwiftParser.TopLevelDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_topLevelDecl)
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.importDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.typeDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.funcDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 95
                self.varDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 96
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(SwiftParser.IMPORT, 0)

        def importPath(self):
            return self.getTypedRuleContext(SwiftParser.ImportPathContext,0)


        def getRuleIndex(self):
            return SwiftParser.RULE_importDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportDecl" ):
                listener.enterImportDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportDecl" ):
                listener.exitImportDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportDecl" ):
                return visitor.visitImportDecl(self)
            else:
                return visitor.visitChildren(self)




    def importDecl(self):

        localctx = SwiftParser.ImportDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_importDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(SwiftParser.IMPORT)
            self.state = 100
            self.importPath()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportPathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.IDENT)
            else:
                return self.getToken(SwiftParser.IDENT, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.DOT)
            else:
                return self.getToken(SwiftParser.DOT, i)

        def getRuleIndex(self):
            return SwiftParser.RULE_importPath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportPath" ):
                listener.enterImportPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportPath" ):
                listener.exitImportPath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportPath" ):
                return visitor.visitImportPath(self)
            else:
                return visitor.visitChildren(self)




    def importPath(self):

        localctx = SwiftParser.ImportPathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_importPath)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(SwiftParser.IDENT)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 103
                self.match(SwiftParser.DOT)
                self.state = 104
                self.match(SwiftParser.IDENT)
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SwiftParser.IDENT, 0)

        def typeBody(self):
            return self.getTypedRuleContext(SwiftParser.TypeBodyContext,0)


        def CLASS(self):
            return self.getToken(SwiftParser.CLASS, 0)

        def STRUCT(self):
            return self.getToken(SwiftParser.STRUCT, 0)

        def ENUM(self):
            return self.getToken(SwiftParser.ENUM, 0)

        def PROTOCOL(self):
            return self.getToken(SwiftParser.PROTOCOL, 0)

        def EXTENSION(self):
            return self.getToken(SwiftParser.EXTENSION, 0)

        def getRuleIndex(self):
            return SwiftParser.RULE_typeDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeDecl" ):
                listener.enterTypeDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeDecl" ):
                listener.exitTypeDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDecl" ):
                return visitor.visitTypeDecl(self)
            else:
                return visitor.visitChildren(self)




    def typeDecl(self):

        localctx = SwiftParser.TypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_typeDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 111
            self.match(SwiftParser.IDENT)
            self.state = 112
            self.typeBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(SwiftParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(SwiftParser.RBRACE, 0)

        def typeMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwiftParser.TypeMemberContext)
            else:
                return self.getTypedRuleContext(SwiftParser.TypeMemberContext,i)


        def getRuleIndex(self):
            return SwiftParser.RULE_typeBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeBody" ):
                listener.enterTypeBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeBody" ):
                listener.exitTypeBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeBody" ):
                return visitor.visitTypeBody(self)
            else:
                return visitor.visitChildren(self)




    def typeBody(self):

        localctx = SwiftParser.TypeBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typeBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(SwiftParser.LBRACE)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4616295187814161600) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 245) != 0):
                self.state = 115
                self.typeMember()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 121
            self.match(SwiftParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcDecl(self):
            return self.getTypedRuleContext(SwiftParser.FuncDeclContext,0)


        def initDecl(self):
            return self.getTypedRuleContext(SwiftParser.InitDeclContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(SwiftParser.VarDeclContext,0)


        def stmt(self):
            return self.getTypedRuleContext(SwiftParser.StmtContext,0)


        def getRuleIndex(self):
            return SwiftParser.RULE_typeMember

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeMember" ):
                listener.enterTypeMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeMember" ):
                listener.exitTypeMember(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeMember" ):
                return visitor.visitTypeMember(self)
            else:
                return visitor.visitChildren(self)




    def typeMember(self):

        localctx = SwiftParser.TypeMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typeMember)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.funcDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.initDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.varDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(SwiftParser.FUNC, 0)

        def IDENT(self):
            return self.getToken(SwiftParser.IDENT, 0)

        def paramClause(self):
            return self.getTypedRuleContext(SwiftParser.ParamClauseContext,0)


        def block(self):
            return self.getTypedRuleContext(SwiftParser.BlockContext,0)


        def returnClause(self):
            return self.getTypedRuleContext(SwiftParser.ReturnClauseContext,0)


        def getRuleIndex(self):
            return SwiftParser.RULE_funcDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDecl" ):
                listener.enterFuncDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDecl" ):
                listener.exitFuncDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = SwiftParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(SwiftParser.FUNC)
            self.state = 130
            self.match(SwiftParser.IDENT)
            self.state = 131
            self.paramClause()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 132
                self.returnClause()


            self.state = 135
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INIT(self):
            return self.getToken(SwiftParser.INIT, 0)

        def paramClause(self):
            return self.getTypedRuleContext(SwiftParser.ParamClauseContext,0)


        def block(self):
            return self.getTypedRuleContext(SwiftParser.BlockContext,0)


        def getRuleIndex(self):
            return SwiftParser.RULE_initDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitDecl" ):
                listener.enterInitDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitDecl" ):
                listener.exitInitDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitDecl" ):
                return visitor.visitInitDecl(self)
            else:
                return visitor.visitChildren(self)




    def initDecl(self):

        localctx = SwiftParser.InitDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_initDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(SwiftParser.INIT)
            self.state = 138
            self.paramClause()
            self.state = 139
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(SwiftParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SwiftParser.RPAREN, 0)

        def paramList(self):
            return self.getTypedRuleContext(SwiftParser.ParamListContext,0)


        def getRuleIndex(self):
            return SwiftParser.RULE_paramClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamClause" ):
                listener.enterParamClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamClause" ):
                listener.exitParamClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamClause" ):
                return visitor.visitParamClause(self)
            else:
                return visitor.visitChildren(self)




    def paramClause(self):

        localctx = SwiftParser.ParamClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paramClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(SwiftParser.LPAREN)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==71:
                self.state = 142
                self.paramList()


            self.state = 145
            self.match(SwiftParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwiftParser.ParamContext)
            else:
                return self.getTypedRuleContext(SwiftParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.COMMA)
            else:
                return self.getToken(SwiftParser.COMMA, i)

        def getRuleIndex(self):
            return SwiftParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = SwiftParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.param()
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==56:
                self.state = 148
                self.match(SwiftParser.COMMA)
                self.state = 149
                self.param()
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeRef(self):
            return self.getTypedRuleContext(SwiftParser.TypeRefContext,0)


        def IDENT(self):
            return self.getToken(SwiftParser.IDENT, 0)

        def COLON(self):
            return self.getToken(SwiftParser.COLON, 0)

        def ASSIGN(self):
            return self.getToken(SwiftParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(SwiftParser.ExprContext,0)


        def getRuleIndex(self):
            return SwiftParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = SwiftParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 155
                self.match(SwiftParser.IDENT)
                self.state = 156
                self.match(SwiftParser.COLON)


            self.state = 159
            self.typeRef()
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 160
                self.match(SwiftParser.ASSIGN)
                self.state = 161
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARROW(self):
            return self.getToken(SwiftParser.ARROW, 0)

        def typeRef(self):
            return self.getTypedRuleContext(SwiftParser.TypeRefContext,0)


        def getRuleIndex(self):
            return SwiftParser.RULE_returnClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnClause" ):
                listener.enterReturnClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnClause" ):
                listener.exitReturnClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnClause" ):
                return visitor.visitReturnClause(self)
            else:
                return visitor.visitChildren(self)




    def returnClause(self):

        localctx = SwiftParser.ReturnClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_returnClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(SwiftParser.ARROW)
            self.state = 165
            self.typeRef()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeRefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.IDENT)
            else:
                return self.getToken(SwiftParser.IDENT, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.DOT)
            else:
                return self.getToken(SwiftParser.DOT, i)

        def typeSuffix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwiftParser.TypeSuffixContext)
            else:
                return self.getTypedRuleContext(SwiftParser.TypeSuffixContext,i)


        def getRuleIndex(self):
            return SwiftParser.RULE_typeRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeRef" ):
                listener.enterTypeRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeRef" ):
                listener.exitTypeRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeRef" ):
                return visitor.visitTypeRef(self)
            else:
                return visitor.visitChildren(self)




    def typeRef(self):

        localctx = SwiftParser.TypeRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_typeRef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(SwiftParser.IDENT)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 168
                self.match(SwiftParser.DOT)
                self.state = 169
                self.match(SwiftParser.IDENT)
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 175
                    self.typeSuffix() 
                self.state = 180
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUESTION(self):
            return self.getToken(SwiftParser.QUESTION, 0)

        def LBRACK(self):
            return self.getToken(SwiftParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(SwiftParser.RBRACK, 0)

        def getRuleIndex(self):
            return SwiftParser.RULE_typeSuffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSuffix" ):
                listener.enterTypeSuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSuffix" ):
                listener.exitTypeSuffix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSuffix" ):
                return visitor.visitTypeSuffix(self)
            else:
                return visitor.visitChildren(self)




    def typeSuffix(self):

        localctx = SwiftParser.TypeSuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_typeSuffix)
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(SwiftParser.QUESTION)
                pass
            elif token in [66]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.match(SwiftParser.LBRACK)
                self.state = 183
                self.match(SwiftParser.RBRACK)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self):
            return self.getTypedRuleContext(SwiftParser.PatternContext,0)


        def LET(self):
            return self.getToken(SwiftParser.LET, 0)

        def VAR(self):
            return self.getToken(SwiftParser.VAR, 0)

        def COLON(self):
            return self.getToken(SwiftParser.COLON, 0)

        def typeRef(self):
            return self.getTypedRuleContext(SwiftParser.TypeRefContext,0)


        def ASSIGN(self):
            return self.getToken(SwiftParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(SwiftParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(SwiftParser.SEMI, 0)

        def getRuleIndex(self):
            return SwiftParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = SwiftParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 187
            self.pattern()
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 188
                self.match(SwiftParser.COLON)
                self.state = 189
                self.typeRef()


            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 192
                self.match(SwiftParser.ASSIGN)
                self.state = 193
                self.expr()


            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 196
                self.match(SwiftParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SwiftParser.IDENT, 0)

        def getRuleIndex(self):
            return SwiftParser.RULE_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPattern" ):
                listener.enterPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPattern" ):
                listener.exitPattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPattern" ):
                return visitor.visitPattern(self)
            else:
                return visitor.visitChildren(self)




    def pattern(self):

        localctx = SwiftParser.PatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(SwiftParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(SwiftParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(SwiftParser.RBRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwiftParser.StmtContext)
            else:
                return self.getTypedRuleContext(SwiftParser.StmtContext,i)


        def getRuleIndex(self):
            return SwiftParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = SwiftParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(SwiftParser.LBRACE)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & 4418035735592435847) != 0):
                self.state = 202
                self.stmt()
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 208
            self.match(SwiftParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStmt(self):
            return self.getTypedRuleContext(SwiftParser.IfStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(SwiftParser.ReturnStmtContext,0)


        def exprStmt(self):
            return self.getTypedRuleContext(SwiftParser.ExprStmtContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(SwiftParser.VarDeclContext,0)


        def block(self):
            return self.getTypedRuleContext(SwiftParser.BlockContext,0)


        def getRuleIndex(self):
            return SwiftParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = SwiftParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmt)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.ifStmt()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.returnStmt()
                pass
            elif token in [29, 30, 31, 32, 33, 45, 46, 52, 62, 66, 68, 69, 70, 71]:
                self.enterOuterAlt(localctx, 3)
                self.state = 212
                self.exprStmt()
                pass
            elif token in [10, 11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 213
                self.varDecl()
                pass
            elif token in [64]:
                self.enterOuterAlt(localctx, 5)
                self.state = 214
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(SwiftParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(SwiftParser.ExprContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwiftParser.BlockContext)
            else:
                return self.getTypedRuleContext(SwiftParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(SwiftParser.ELSE, 0)

        def ifStmt(self):
            return self.getTypedRuleContext(SwiftParser.IfStmtContext,0)


        def getRuleIndex(self):
            return SwiftParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = SwiftParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(SwiftParser.IF)
            self.state = 218
            self.expr()
            self.state = 219
            self.block()
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 220
                self.match(SwiftParser.ELSE)
                self.state = 223
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [64]:
                    self.state = 221
                    self.block()
                    pass
                elif token in [17]:
                    self.state = 222
                    self.ifStmt()
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(SwiftParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(SwiftParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(SwiftParser.SEMI, 0)

        def getRuleIndex(self):
            return SwiftParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = SwiftParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(SwiftParser.RETURN)
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 228
                self.expr()


            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 231
                self.match(SwiftParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SwiftParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(SwiftParser.SEMI, 0)

        def getRuleIndex(self):
            return SwiftParser.RULE_exprStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStmt" ):
                listener.enterExprStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStmt" ):
                listener.exitExprStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)




    def exprStmt(self):

        localctx = SwiftParser.ExprStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exprStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.expr()
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 235
                self.match(SwiftParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignExpr(self):
            return self.getTypedRuleContext(SwiftParser.AssignExprContext,0)


        def getRuleIndex(self):
            return SwiftParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = SwiftParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.assignExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalExpr(self):
            return self.getTypedRuleContext(SwiftParser.ConditionalExprContext,0)


        def ASSIGN(self):
            return self.getToken(SwiftParser.ASSIGN, 0)

        def assignExpr(self):
            return self.getTypedRuleContext(SwiftParser.AssignExprContext,0)


        def getRuleIndex(self):
            return SwiftParser.RULE_assignExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignExpr" ):
                listener.enterAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignExpr" ):
                listener.exitAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpr" ):
                return visitor.visitAssignExpr(self)
            else:
                return visitor.visitChildren(self)




    def assignExpr(self):

        localctx = SwiftParser.AssignExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assignExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.conditionalExpr()
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 241
                self.match(SwiftParser.ASSIGN)
                self.state = 242
                self.assignExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpr(self):
            return self.getTypedRuleContext(SwiftParser.LogicalOrExprContext,0)


        def getRuleIndex(self):
            return SwiftParser.RULE_conditionalExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalExpr" ):
                listener.enterConditionalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalExpr" ):
                listener.exitConditionalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalExpr" ):
                return visitor.visitConditionalExpr(self)
            else:
                return visitor.visitChildren(self)




    def conditionalExpr(self):

        localctx = SwiftParser.ConditionalExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_conditionalExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.logicalOrExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwiftParser.LogicalAndExprContext)
            else:
                return self.getTypedRuleContext(SwiftParser.LogicalAndExprContext,i)


        def OR_OR(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.OR_OR)
            else:
                return self.getToken(SwiftParser.OR_OR, i)

        def getRuleIndex(self):
            return SwiftParser.RULE_logicalOrExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpr" ):
                listener.enterLogicalOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpr" ):
                listener.exitLogicalOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpr" ):
                return visitor.visitLogicalOrExpr(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrExpr(self):

        localctx = SwiftParser.LogicalOrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_logicalOrExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.logicalAndExpr()
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 248
                self.match(SwiftParser.OR_OR)
                self.state = 249
                self.logicalAndExpr()
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwiftParser.EqualityExprContext)
            else:
                return self.getTypedRuleContext(SwiftParser.EqualityExprContext,i)


        def AND_AND(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.AND_AND)
            else:
                return self.getToken(SwiftParser.AND_AND, i)

        def getRuleIndex(self):
            return SwiftParser.RULE_logicalAndExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpr" ):
                listener.enterLogicalAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpr" ):
                listener.exitLogicalAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpr" ):
                return visitor.visitLogicalAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def logicalAndExpr(self):

        localctx = SwiftParser.LogicalAndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_logicalAndExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.equalityExpr()
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 256
                self.match(SwiftParser.AND_AND)
                self.state = 257
                self.equalityExpr()
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwiftParser.RelationalExprContext)
            else:
                return self.getTypedRuleContext(SwiftParser.RelationalExprContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.EQ)
            else:
                return self.getToken(SwiftParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.NEQ)
            else:
                return self.getToken(SwiftParser.NEQ, i)

        def getRuleIndex(self):
            return SwiftParser.RULE_equalityExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpr" ):
                listener.enterEqualityExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpr" ):
                listener.exitEqualityExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpr" ):
                return visitor.visitEqualityExpr(self)
            else:
                return visitor.visitChildren(self)




    def equalityExpr(self):

        localctx = SwiftParser.EqualityExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_equalityExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.relationalExpr()
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40 or _la==41:
                self.state = 264
                _la = self._input.LA(1)
                if not(_la==40 or _la==41):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 265
                self.relationalExpr()
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwiftParser.AdditiveExprContext)
            else:
                return self.getTypedRuleContext(SwiftParser.AdditiveExprContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.LT)
            else:
                return self.getToken(SwiftParser.LT, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.LE)
            else:
                return self.getToken(SwiftParser.LE, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.GT)
            else:
                return self.getToken(SwiftParser.GT, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.GE)
            else:
                return self.getToken(SwiftParser.GE, i)

        def getRuleIndex(self):
            return SwiftParser.RULE_relationalExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpr" ):
                listener.enterRelationalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpr" ):
                listener.exitRelationalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpr(self):

        localctx = SwiftParser.RelationalExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_relationalExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.additiveExpr()
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3378524354248704) != 0):
                self.state = 272
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3378524354248704) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 273
                self.additiveExpr()
                self.state = 278
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwiftParser.MultiplicativeExprContext)
            else:
                return self.getTypedRuleContext(SwiftParser.MultiplicativeExprContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.PLUS)
            else:
                return self.getToken(SwiftParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.MINUS)
            else:
                return self.getToken(SwiftParser.MINUS, i)

        def getRuleIndex(self):
            return SwiftParser.RULE_additiveExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpr(self):

        localctx = SwiftParser.AdditiveExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_additiveExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.multiplicativeExpr()
            self.state = 284
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 280
                    _la = self._input.LA(1)
                    if not(_la==45 or _la==46):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 281
                    self.multiplicativeExpr() 
                self.state = 286
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwiftParser.UnaryExprContext)
            else:
                return self.getTypedRuleContext(SwiftParser.UnaryExprContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.STAR)
            else:
                return self.getToken(SwiftParser.STAR, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.DIV)
            else:
                return self.getToken(SwiftParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.MOD)
            else:
                return self.getToken(SwiftParser.MOD, i)

        def getRuleIndex(self):
            return SwiftParser.RULE_multiplicativeExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpr" ):
                listener.enterMultiplicativeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpr" ):
                listener.exitMultiplicativeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpr" ):
                return visitor.visitMultiplicativeExpr(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpr(self):

        localctx = SwiftParser.MultiplicativeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_multiplicativeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.unaryExpr()
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 985162418487296) != 0):
                self.state = 288
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 985162418487296) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 289
                self.unaryExpr()
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfixExpr(self):
            return self.getTypedRuleContext(SwiftParser.PostfixExprContext,0)


        def NOT(self):
            return self.getToken(SwiftParser.NOT, 0)

        def MINUS(self):
            return self.getToken(SwiftParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(SwiftParser.PLUS, 0)

        def getRuleIndex(self):
            return SwiftParser.RULE_unaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = SwiftParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4609152743636992) != 0):
                self.state = 295
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4609152743636992) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 298
            self.postfixExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpr(self):
            return self.getTypedRuleContext(SwiftParser.PrimaryExprContext,0)


        def postfixOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwiftParser.PostfixOpContext)
            else:
                return self.getTypedRuleContext(SwiftParser.PostfixOpContext,i)


        def getRuleIndex(self):
            return SwiftParser.RULE_postfixExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfixExpr" ):
                listener.enterPostfixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfixExpr" ):
                listener.exitPostfixExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixExpr" ):
                return visitor.visitPostfixExpr(self)
            else:
                return visitor.visitChildren(self)




    def postfixExpr(self):

        localctx = SwiftParser.PostfixExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_postfixExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.primaryExpr()
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 301
                    self.postfixOp() 
                self.state = 306
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memberAccess(self):
            return self.getTypedRuleContext(SwiftParser.MemberAccessContext,0)


        def callSuffix(self):
            return self.getTypedRuleContext(SwiftParser.CallSuffixContext,0)


        def optionalChain(self):
            return self.getTypedRuleContext(SwiftParser.OptionalChainContext,0)


        def getRuleIndex(self):
            return SwiftParser.RULE_postfixOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfixOp" ):
                listener.enterPostfixOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfixOp" ):
                listener.exitPostfixOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixOp" ):
                return visitor.visitPostfixOp(self)
            else:
                return visitor.visitChildren(self)




    def postfixOp(self):

        localctx = SwiftParser.PostfixOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_postfixOp)
        try:
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.memberAccess()
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.callSuffix()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 309
                self.optionalChain()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(SwiftParser.DOT, 0)

        def IDENT(self):
            return self.getToken(SwiftParser.IDENT, 0)

        def getRuleIndex(self):
            return SwiftParser.RULE_memberAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberAccess" ):
                listener.enterMemberAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberAccess" ):
                listener.exitMemberAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberAccess" ):
                return visitor.visitMemberAccess(self)
            else:
                return visitor.visitChildren(self)




    def memberAccess(self):

        localctx = SwiftParser.MemberAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_memberAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(SwiftParser.DOT)
            self.state = 313
            self.match(SwiftParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionalChainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPTIONAL_CHAIN(self):
            return self.getToken(SwiftParser.OPTIONAL_CHAIN, 0)

        def IDENT(self):
            return self.getToken(SwiftParser.IDENT, 0)

        def getRuleIndex(self):
            return SwiftParser.RULE_optionalChain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptionalChain" ):
                listener.enterOptionalChain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptionalChain" ):
                listener.exitOptionalChain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptionalChain" ):
                return visitor.visitOptionalChain(self)
            else:
                return visitor.visitChildren(self)




    def optionalChain(self):

        localctx = SwiftParser.OptionalChainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_optionalChain)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(SwiftParser.OPTIONAL_CHAIN)
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 316
                self.match(SwiftParser.IDENT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallSuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(SwiftParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SwiftParser.RPAREN, 0)

        def argList(self):
            return self.getTypedRuleContext(SwiftParser.ArgListContext,0)


        def getRuleIndex(self):
            return SwiftParser.RULE_callSuffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallSuffix" ):
                listener.enterCallSuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallSuffix" ):
                listener.exitCallSuffix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallSuffix" ):
                return visitor.visitCallSuffix(self)
            else:
                return visitor.visitChildren(self)




    def callSuffix(self):

        localctx = SwiftParser.CallSuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_callSuffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(SwiftParser.LPAREN)
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 29)) & ~0x3f) == 0 and ((1 << (_la - 29)) & 8392374681631) != 0):
                self.state = 320
                self.argList()


            self.state = 323
            self.match(SwiftParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwiftParser.ArgContext)
            else:
                return self.getTypedRuleContext(SwiftParser.ArgContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.COMMA)
            else:
                return self.getToken(SwiftParser.COMMA, i)

        def getRuleIndex(self):
            return SwiftParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = SwiftParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.arg()
            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==56:
                self.state = 326
                self.match(SwiftParser.COMMA)
                self.state = 327
                self.arg()
                self.state = 332
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SwiftParser.ExprContext,0)


        def IDENT(self):
            return self.getToken(SwiftParser.IDENT, 0)

        def COLON(self):
            return self.getToken(SwiftParser.COLON, 0)

        def getRuleIndex(self):
            return SwiftParser.RULE_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg" ):
                listener.enterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg" ):
                listener.exitArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = SwiftParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 333
                self.match(SwiftParser.IDENT)
                self.state = 334
                self.match(SwiftParser.COLON)


            self.state = 337
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(SwiftParser.LiteralContext,0)


        def SELF(self):
            return self.getToken(SwiftParser.SELF, 0)

        def SUPER(self):
            return self.getToken(SwiftParser.SUPER, 0)

        def IDENT(self):
            return self.getToken(SwiftParser.IDENT, 0)

        def LPAREN(self):
            return self.getToken(SwiftParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(SwiftParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(SwiftParser.RPAREN, 0)

        def collectionLiteral(self):
            return self.getTypedRuleContext(SwiftParser.CollectionLiteralContext,0)


        def getRuleIndex(self):
            return SwiftParser.RULE_primaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpr" ):
                listener.enterPrimaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpr" ):
                listener.exitPrimaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpr(self):

        localctx = SwiftParser.PrimaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_primaryExpr)
        try:
            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31, 32, 33, 68, 69, 70]:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.literal()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.match(SwiftParser.SELF)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 341
                self.match(SwiftParser.SUPER)
                pass
            elif token in [71]:
                self.enterOuterAlt(localctx, 4)
                self.state = 342
                self.match(SwiftParser.IDENT)
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 5)
                self.state = 343
                self.match(SwiftParser.LPAREN)
                self.state = 344
                self.expr()
                self.state = 345
                self.match(SwiftParser.RPAREN)
                pass
            elif token in [66]:
                self.enterOuterAlt(localctx, 6)
                self.state = 347
                self.collectionLiteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CollectionLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(SwiftParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(SwiftParser.RBRACK, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwiftParser.ExprContext)
            else:
                return self.getTypedRuleContext(SwiftParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SwiftParser.COMMA)
            else:
                return self.getToken(SwiftParser.COMMA, i)

        def getRuleIndex(self):
            return SwiftParser.RULE_collectionLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCollectionLiteral" ):
                listener.enterCollectionLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCollectionLiteral" ):
                listener.exitCollectionLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCollectionLiteral" ):
                return visitor.visitCollectionLiteral(self)
            else:
                return visitor.visitChildren(self)




    def collectionLiteral(self):

        localctx = SwiftParser.CollectionLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_collectionLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(SwiftParser.LBRACK)
            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 29)) & ~0x3f) == 0 and ((1 << (_la - 29)) & 8392374681631) != 0):
                self.state = 351
                self.expr()
                self.state = 356
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==56:
                    self.state = 352
                    self.match(SwiftParser.COMMA)
                    self.state = 353
                    self.expr()
                    self.state = 358
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 361
            self.match(SwiftParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SwiftParser.STRING, 0)

        def INT(self):
            return self.getToken(SwiftParser.INT, 0)

        def FLOAT(self):
            return self.getToken(SwiftParser.FLOAT, 0)

        def TRUE(self):
            return self.getToken(SwiftParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(SwiftParser.FALSE, 0)

        def NIL(self):
            return self.getToken(SwiftParser.NIL, 0)

        def getRuleIndex(self):
            return SwiftParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = SwiftParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            _la = self._input.LA(1)
            if not(((((_la - 31)) & ~0x3f) == 0 and ((1 << (_la - 31)) & 962072674311) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





