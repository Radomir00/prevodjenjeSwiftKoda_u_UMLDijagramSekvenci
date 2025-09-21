lexer grammar SwiftLexer;

// --- Keywords ---
CLASS      : 'class';
EXTENSION  : 'extension';
FUNC       : 'func';
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
WHILE      : 'while';
REPEAT     : 'repeat';
FOR        : 'for';
IN         : 'in';
DO         : 'do';
CATCH      : 'catch';
SWITCH     : 'switch';
CASE       : 'case';
DEFAULT    : 'default';
THROWS     : 'throws';
RETHROWS   : 'rethrows';
SELF       : 'self';
SUPER      : 'super';
TRUE       : 'true';
FALSE      : 'false';
NIL        : 'nil';
IMPORT    : 'import';

// --- Operators / punctuation (order matters: longer first) ---
RANGE_CLOSED    : '...';
RANGE_HALFOPEN  : '..<';
SAFE_NAV        : '?.';
NULL_COALESCING : '??';
ARROW           : '->';

EQEQ        : '==';
TRIPLE_EQ   : '===';
NEQ         : '!=';
TRIPLE_NEQ  : '!==';
LEQ         : '<=';
GEQ         : '>=';
LSHIFT      : '<<';
RSHIFT      : '>>';
ANDAND      : '&&';
OROR        : '||';

ASSIGN      : '=';
PLUS        : '+';
MINUS       : '-';
MUL         : '*';
DIV         : '/';
MOD         : '%';
LT          : '<';
GT          : '>';
BITAND      : '&';
BITOR       : '|';
BITXOR      : '^';
NOT         : '!';
QUESTION    : '?';
DOT         : '.';
COMMA       : ',';
COLON       : ':';
SEMI        : ';';
LPAREN      : '(';
RPAREN      : ')';
LBRACE      : '{';
RBRACE      : '}';
LBRACK      : '[';
RBRACK      : ']';

// --- Literals & identifiers ---
INT   : [0-9]+;
FLOAT : [0-9]+ '.' [0-9]+ | '.' [0-9]+ ;

STRING
  : '"' ( '\\' . | ~["\\\r\n] )* '"'
  ;

IDENT : [A-Za-z_][A-Za-z_0-9]*;

// --- Whitespace & comments ---
LINE_COMMENT  : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT : '/*' .*? '*/'  -> skip;
WS            : [ \t\r\n]+     -> skip;
