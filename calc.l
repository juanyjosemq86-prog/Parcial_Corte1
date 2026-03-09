%{
#include "calc.tab.h"
#include <stdlib.h>
%}

%%

[0-9]+(\.[0-9]+)? { yylval = atof(yytext); return NUMBER; }
sqrt              { return SQRT; }
\n                { return EOL; }

[ \t] ;

. return yytext[0];

%%

int yywrap(){
 return 1;
}
