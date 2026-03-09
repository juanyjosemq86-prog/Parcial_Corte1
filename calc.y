%{
#include <stdio.h>
#include <math.h>

int yylex();
int yyerror(const char *s);

double newton(double n);

%}

%token NUMBER SQRT
%token EOL

%%

input:
      | input line
;

line:
      SQRT NUMBER EOL { printf("Resultado: %lf\n", newton($2)); }
;

%%

double newton(double n){

 double x = n;
 double error = 0.00001;
 double raiz;

 while(1){

  raiz = 0.5 * (x + n/x);

  if(fabs(raiz - x) < error)
      break;

  x = raiz;
 }

 return raiz;
}

int main(){
 printf("Calculadora de raiz cuadrada (Newton-Raphson)\n");
 yyparse();
 return 0;
}

int yyerror(const char *s){
 printf("Error: %s\n", s);
 return 0;
}
