grammar FlowLang;

program
    : step+ EOF
    ;

step
    : INICIO ';'                     # inicioStep
    | PROCESO ID ':' expr ';'        # procesoStep
    | control                         # controlStep
    ;

control
    : SI expr ':' step (SINO ':' step)?
    ;

expr
    : ID comparator NUMBER            # exprComp
    | NUMBER                          # exprNum
    ;

comparator
    : '>'
    | '<'
    | '>='
    | '<='
    | '=='
    | '!='
    ;

INICIO  : 'Inicio' ;
PROCESO : 'Proceso' ;
SI      : 'Si' ;
SINO    : 'Sino' ;

PLUS    : '+' ;
MINUS   : '-' ;
TIMES   : '*' ;
DIVIDE  : '/' ;

ID      : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER  : [0-9]+ ;
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;
