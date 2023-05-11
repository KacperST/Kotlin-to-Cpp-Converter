
grammar Expr;

WS: ' ' -> skip;

ADD: '+';
SUBSTRACT: '-';
MULTIPLY: '*';
DIVIDE:  '/';
RANGE: '..';
MOD: '%';
INCR: '++';
DECR: '--';
DOT: '.';
EQ: '=';
ADD_ASSIGNMENT: '+=';
SUB_ASSIGNMENT: '-=';
MULT_ASSIGNMENT: '*=';
DIV_ASSIGNMENT: '/=';
MOD_ASSIGNMENT: '%=';
COLON: ':';
COMA : ',';
LPAREN: '(';
RPAREN: ')';
LSQUARE: '[';
RSQUARE: ']';
LCURL: '{';
RCURL: '}';
LTHAN: '<';
GTHAN: '>';
LE: '<=';
GE: '>=';
EQEQ: '==';
NOTEQ: '!=';
AND: '&&';
OR: '||';
SINGLE_QUOTE: '\'';
IF: 'if';
ELSE: 'else';
FOR: 'for';
WHILE: 'while';
RETURN: 'return';
DOWNTO: 'downTo';
STEP: 'step';
CONTINUE: 'continue';
BREAK: 'break';
PUBLIC: 'public';
PRIVATE: 'private';
PROTECTED: 'protected';
FUN: 'fun';
VAL: 'val';
VAR: 'var';
CLASS: 'class';
IN: 'in';
NEWLINE: [\r\n]+ ;
INT: 'Int';
DOUBLE: 'Double';
//FLOAT: 'Float';
CHAR: 'Char';
STRING: 'String';
BOOLEAN: 'Boolean';
IDENTIFIER: ('a'..'z' | 'A'..'Z') ('0'..'9' | 'a'..'z' | 'A'..'Z')*;
INTLITERAL: ('-'? ('1'..'9')('0'..'9')*) | '0';
DOUBLELITERAL:  ('0'..'9')+ '.' ('0'..'9')+ ;
STRINGLITERAL: UNTERMINATEDSTRINGLITERAL '"';
UNTERMINATEDSTRINGLITERAL : '"' (~["\\\r\n] | '\\' (. | EOF))*;
CHARLITERAL: '"' (~["\\\r\n] | '\\' (. | EOF)) '"';
BOOLEANLITERAL: 'true' | 'false';
INTNUMBER: ('0'..'9');
NULL:  'null';
PRINT: 'print';

prog: (expr NEWLINE*)*;

expr: (variable
    | if_statement
    | for_loop
    | assignment
    | NEWLINE
    | func_or_class_call
    | func_declaration
    | unary
    | class_declaration
    | while_loop);


variable: variable_assign | variable_declaration;
variable_declaration: (VAR|VAL) IDENTIFIER COLON typ (EQ literals)?;
variable_assign: (VAR|VAL)? IDENTIFIER EQ literals;

parameter:  IDENTIFIER COLON typ;

unary_operator: INCR
                | DECR;

unary: IDENTIFIER unary_operator;

operators: MULTIPLY
            | DIVIDE
            | ADD
            | SUBSTRACT;


logic_operators: AND
                | OR;

numeric_literals: numeric_type operators numeric_type
        | numeric_type;

text_type: text_type  ADD text_type
        | STRINGLITERAL
        | CHARLITERAL
        | IDENTIFIER;

numeric_type:   INTLITERAL
              | DOUBLELITERAL
              | IDENTIFIER;


literals:   BOOLEANLITERAL
        | text_type
        | numeric_literals
        | func_or_class_call
        | IDENTIFIER
        | NULL;

assignment_type:  ADD_ASSIGNMENT
                | SUB_ASSIGNMENT
                | MULT_ASSIGNMENT
                | DIV_ASSIGNMENT;

assignment: IDENTIFIER assignment_type literals;

comparisson_type: EQEQ
          | LE
          | GE
          | GTHAN
          | LTHAN
          | NOTEQ;


typ:  INT
    | DOUBLE
    | STRING
    | CHAR
    | IDENTIFIER
    | BOOLEAN;

if_statement: IF LPAREN if_body RPAREN LCURL NEWLINE*
                expr*
                (BREAK | CONTINUE)? NEWLINE*
                RCURL NEWLINE*  (ELSE if_statement |
                         ELSE LCURL NEWLINE* expr* (BREAK | CONTINUE)? RCURL NEWLINE* )?;

if_body: literals comparisson_type literals
        | if_body logic_operators if_body;

func_declaration: visibility_modifier? FUN IDENTIFIER class_or_func_body (COLON typ)? LCURL NEWLINE*
                    expr*
                    (RETURN literals NEWLINE?)?
                    RCURL;

for_loop_condition: INTLITERAL  (RANGE|DOWNTO)  INTLITERAL (STEP (INTLITERAL))?;

for_loop: FOR LPAREN IDENTIFIER IN for_loop_condition RPAREN LCURL NEWLINE*
            expr*
            RCURL;

while_loop: WHILE LPAREN while_condition RPAREN LCURL NEWLINE*
            expr*
            RCURL;

while_condition: (literals comparisson_type literals) | IDENTIFIER;

visibility_modifier:  PUBLIC
                    | PROTECTED
                    | PRIVATE;

class_or_func_body: LPAREN ((parameter COMA)* parameter)? RPAREN;


class_declaration: visibility_modifier? CLASS IDENTIFIER class_or_func_body LCURL  NEWLINE*
                    (visibility_modifier? variable_declaration NEWLINE* )*
                    (visibility_modifier? func_declaration NEWLINE* )*
                    RCURL;

func_or_class_call:  IDENTIFIER  LPAREN ((literals COMA)* literals)? RPAREN NEWLINE*
                    | IDENTIFIER DOT func_or_class_call;

