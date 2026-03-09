grammar fibonacci;

prog: 'FIBO' '(' NUMBER ')' EOF;

NUMBER: [0-9]+;

WS: [ \t\r\n]+ -> skip;
