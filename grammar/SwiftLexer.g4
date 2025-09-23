lexer grammar SwiftLexer;

// --- Keywords we actually need for sequence extraction ---
CLASS      : 'class';
STRUCT     : 'struct';
ENUM       : 'enum';
EXTENSION  : 'extension';
PROTOCOL   : 'protocol';
FUNC       : 'func';
INIT       : 'init';
DEINIT     : 'deinit';
STATIC     : 'static';
LET        : 'let';
VAR        : 'var';
RETURN     : 'return';
BREAK      : 'break';
CONTINUE   : 'continue';
THROW      : 'throw';
TRY        : 'try';
IF         : 'if';
ELSE       : 'else';
FOR        : 'for';
WHILE      : 'while';
REPEAT     : 'repeat';
DO         : 'do';
SWITCH     : 'switch';
CASE       : 'case';
DEFAULT    : 'default';
GUARD      : 'guard';
WHERE      : 'where';
IMPORT     : 'import';
SELF       : 'self';
SUPER      : 'super';
TRUE       : 'true';
FALSE      : 'false';
NIL        : 'nil';

// --- Operators & punctuation (order matters: longer tokens first) ---
OPTIONAL_CHAIN : '?.';
RANGE_CLOSED   : '...';
RANGE_HALF     : '..<';
ARROW          : '->';
LE             : '<=';
GE             : '>=';
EQ             : '==';
NEQ            : '!=';
AND_AND        : '&&';
OR_OR          : '||';
ASSIGN         : '=';
PLUS           : '+';
MINUS          : '-';
STAR           : '*';
DIV            : '/';
MOD            : '%';
LT             : '<';
GT             : '>';
NOT            : '!';
QUESTION       : '?';
COLON          : ':';
SEMI           : ';';
COMMA          : ',';
DOT            : '.';
AT             : '@';
AMP            : '&';
PIPE           : '|';
AROB           : '#';

LPAREN         : '(';
RPAREN         : ')';
LBRACE         : '{';
RBRACE         : '}';
LBRACK         : '[';
RBRACK         : ']';

// --- Literals & identifiers ---
FLOAT
  : [0-9]+ '.' [0-9]+ ([eE] [+\-]? [0-9]+)?    // 12.34, 12.34e-2
  | '.' [0-9]+ ([eE] [+\-]? [0-9]+)?           // .5, .5e1
  | [0-9]+ [eE] [+\-]? [0-9]+                  // 1e9
  ;

INT
  : [0-9]+
  ;

STRING
  : '"' ( '\\' . | ~["\\\r\n] )* '"'
  ;

IDENT
  : '`' (~[`\\\r\n])+ '`'
  | [A-Za-z_][A-Za-z_0-9]*
  ;

// --- Comments & whitespace ---
LINE_COMMENT  : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT : '/*' .*? '*/' -> skip;
WS            : [ \t\r\n\u000C]+ -> skip;
