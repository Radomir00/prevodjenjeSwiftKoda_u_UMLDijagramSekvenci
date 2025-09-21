parser grammar SwiftParser;

options { tokenVocab=SwiftLexer; }

program
  : (declOrStmt)* EOF
  ;

declOrStmt
  : importStmt
  | classDecl
  | extensionDecl
  | funcDecl
  | statement
  ;

importStmt
  : IMPORT IDENT (DOT IDENT)* SEMI?
  ;

// --- Declarations ---
classDecl
  : CLASS IDENT LBRACE member* RBRACE SEMI?
  ;

extensionDecl
  : EXTENSION IDENT LBRACE member* RBRACE
  ;

member
  : funcDecl
  | varDecl
  | statement
  ;

funcDecl
  : (STATIC)? FUNC IDENT LPAREN parameterList? RPAREN
    (THROWS | RETHROWS)? (ARROW type)?
    block
  ;

parameterList
  : parameter (COMMA parameter)*
  ;

parameter
  : IDENT (COLON type)?
  ;

// zadržavamo tip jednostavno (IDENT)
type
  : IDENT
  ;

// --- Empty / no-op statement ---
emptyStmt
  : SEMI
  ;

// --- Statements ---
statement
  : emptyStmt
  | varDecl
  | assignStmt
  | returnStmt
  | breakStmt
  | continueStmt
  | throwStmt
  | ifStmt
  | whileStmt
  | repeatStmt
  | forInStmt
  | doCatchStmt
  | switchStmt
  | exprStatement
  | block
  ;

block
  : LBRACE statement* RBRACE
  ;

varDecl
  : (LET | VAR) IDENT (COLON type)? (ASSIGN expression)? SEMI?
  ;

assignStmt
  : IDENT ASSIGN expression SEMI?
  ;

returnStmt
  : RETURN expression? SEMI?
  ;

breakStmt
  : BREAK SEMI?
  ;

continueStmt
  : CONTINUE SEMI?
  ;

throwStmt
  : THROW expression SEMI?
  ;

// if (expr) { } | if expr { }
ifStmt
  : IF (LPAREN expression RPAREN | expression) block (ELSE block)?
  ;

// while (expr) { } | while expr { }
whileStmt
  : WHILE (LPAREN expression RPAREN | expression) block
  ;

// repeat { } while (expr) | repeat { } while expr
repeatStmt
  : REPEAT block WHILE (LPAREN expression RPAREN | expression) SEMI?
  ;

// for pattern in (range|expr) { }   (bez zagrada)
forInStmt
  : FOR pattern IN (rangeLiteral | expression) block
  ;

pattern
  : IDENT
  ;

rangeLiteral
  : expression RANGE_CLOSED expression
  | expression RANGE_HALFOPEN expression
  ;

doCatchStmt
  : DO block (CATCH block)+
  ;

// switch (expr) { ... } | switch expr { ... }
switchStmt
  : SWITCH (LPAREN expression RPAREN | expression) LBRACE caseClause* defaultClause? RBRACE
  ;

caseClause
  : CASE expression COLON statement*
  ;

defaultClause
  : DEFAULT COLON statement*
  ;

exprStatement
  : expression SEMI?
  ;

// --- Expressions ---
expression
  : TRY expression                           # tryExpr
  | postfixExpr                              # postfixOnly
  ;

postfixExpr
  : primary (postfixSuffix)*
  ;

postfixSuffix
  : callSuffix
  | memberAccess
  ;

callSuffix
  : LPAREN argumentList? RPAREN
  ;

memberAccess
  : (DOT | SAFE_NAV) IDENT (callSuffix)?
  ;

argumentList
  : expression (COMMA expression)*
  ;

primary
  : literal
  | IDENT
  | SELF
  | SUPER
  | LPAREN expression RPAREN
  ;

literal
  : INT
  | FLOAT
  | STRING
  | TRUE
  | FALSE
  | NIL
  ;
