grammar FlowLang;

// ========================================
// REGLA PRINCIPAL
// ========================================

program
    : step+ EOF
    ;

// ========================================
// PASOS
// ========================================

step
    : INICIO ';'                             # inicioStep
    | PROCESO ID ':' expression ';'         # procesoStep
    | control                               # controlStep
    ;

// ========================================
// CONTROL
// ========================================

control
    : SI condition ':' step (SINO ':' step)?
    ;

// ========================================
// CONDICIONES
// ========================================

condition
    : expression comparator expression
    ;

// ========================================
// EXPRESIONES MATEMATICAS
// ========================================

expression
    : expression TIMES expression           # mulExpr
    | expression DIVIDE expression          # divExpr
    | expression PLUS expression            # plusExpr
    | expression MINUS expression           # minusExpr
    | ID                                    # idExpr
    | NUMBER                                # numberExpr
    ;

// ========================================
// COMPARADORES
// ========================================

comparator
    : '>'
    | '<'
    | '>='
    | '<='
    | '=='
    | '!='
    ;

// ========================================
// TOKENS
// ========================================

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
