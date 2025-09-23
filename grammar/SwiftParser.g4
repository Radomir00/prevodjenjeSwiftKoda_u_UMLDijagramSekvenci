parser grammar SwiftParser;

options { tokenVocab=SwiftLexer; }

compilationUnit
  : topLevelDecl* EOF
  ;

topLevelDecl
  : importDecl
  | typeDecl
  | funcDecl
  | varDecl
  | stmt
  ;

importDecl
  : IMPORT importPath
  ;
importPath
  : IDENT (DOT IDENT)*
  ;

// ---- Types: class/struct/enum/protocol ----
typeDecl
  : (CLASS | STRUCT | ENUM | PROTOCOL | EXTENSION) IDENT typeBody
  ;
typeBody
  : LBRACE typeMember* RBRACE
  ;
typeMember
  : funcDecl
  | initDecl
  | varDecl
  | stmt
  ;

// ---- Func / Init ----
funcDecl
  : FUNC IDENT paramClause returnClause? block
  ;
initDecl
  : INIT paramClause block
  ;

paramClause
  : LPAREN paramList? RPAREN
  ;
paramList
  : param (COMMA param)*
  ;
param
  : (IDENT COLON)? typeRef (ASSIGN expr)?   // dozvolimo default
  ;

returnClause
  : ARROW typeRef
  ;

typeRef
  : IDENT (DOT IDENT)* typeSuffix*
  ;
typeSuffix
  : QUESTION             // opcionalni tip: T?
  | LBRACK RBRACK        // npr. T[]
  ;

// ---- Vars (top-level ili u tipu) ----
varDecl
  : (LET | VAR) pattern (COLON typeRef)? (ASSIGN expr)? SEMI?
  ;
pattern
  : IDENT
  ;

// ---- Blocks & statements ----
block
  : LBRACE stmt* RBRACE
  ;

stmt
  : ifStmt
  | returnStmt
  | exprStmt
  | varDecl
  | block
  ;

ifStmt
  : IF expr block (ELSE (block | ifStmt))?
  ;

returnStmt
  : RETURN expr? SEMI?
  ;

exprStmt
  : expr SEMI?
  ;

// ---- Expressions (subset sa jasnim fokusom na pozive) ----
// Gruba, ali praktična hijerarhija:
expr
  : assignExpr
  ;

assignExpr
  : conditionalExpr (ASSIGN assignExpr)?    // right-assoc
  ;

conditionalExpr
  : logicalOrExpr                            // (?: …) izostavljamo – nije nam kritično
  ;

logicalOrExpr
  : logicalAndExpr (OR_OR logicalAndExpr)*
  ;

logicalAndExpr
  : equalityExpr (AND_AND equalityExpr)*
  ;

equalityExpr
  : relationalExpr ((EQ | NEQ) relationalExpr)*
  ;

relationalExpr
  : additiveExpr ((LT | LE | GT | GE) additiveExpr)*
  ;

additiveExpr
  : multiplicativeExpr ((PLUS | MINUS) multiplicativeExpr)*
  ;

multiplicativeExpr
  : unaryExpr ((STAR | DIV | MOD) unaryExpr)*
  ;

unaryExpr
  : (NOT | MINUS | PLUS)? postfixExpr
  ;

postfixExpr
  : primaryExpr postfixOp*
  ;

postfixOp
  : memberAccess
  | callSuffix
  | optionalChain
  ;

memberAccess
  : DOT IDENT
  ;

optionalChain
  : OPTIONAL_CHAIN IDENT?                    // a?.b  ili  a?.
  ;

callSuffix
  : LPAREN argList? RPAREN
  ;

argList
  : arg (COMMA arg)*
  ;
arg
  : (IDENT COLON)? expr
  ;

// ---- Primaries ----
primaryExpr
  : literal
  | SELF
  | SUPER
  | IDENT
  | LPAREN expr RPAREN
  | collectionLiteral
  ;

collectionLiteral
  : LBRACK (expr (COMMA expr)*)? RBRACK
  ;

literal
  : STRING
  | INT
  | FLOAT
  | TRUE
  | FALSE
  | NIL
  ;
