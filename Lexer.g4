lexer grammar Lexer;

PASSWORD: [A-Z] [A-Za-z0-9!@#$&]* [A-Z] [A-Za-z0-9!@#$&]* [a-z] [A-Za-z0-9!@#$&]* [a-z] [A-Za-z0-9!@#$&]* [a-z] [A-Za-z0-9!@#$&]* [0-9] [A-Za-z0-9!@#$&]* [0-9] [A-Za-z0-9!@#$&]* [!@#$&] [A-Za-z0-9!@#$&]* ;

USERNAME: [a-z0-9_-] [a-z0-9_-]{2,15} ;

DECIMAL: '-'? [0-9]+ ('.' [0-9]+)? ;

LETTERS: [a-zA-ZñÑáéíóúÁÉÍÓÚ]+ (' ' [a-zA-ZñÑáéíóúÁÉÍÓÚ]+)* ;

MONEY: [0-9]+ [.,] '00' ;

WS: [ \t\r\n]+ -> skip ;
