#include <stdio.h>
#include <time.h>

long fibonacci(int n){

 if(n<=1)
   return n;

 return fibonacci(n-1) + fibonacci(n-2);
}

int main(){

 int n = 35;

 clock_t inicio = clock();

 long resultado = fibonacci(n);

 clock_t fin = clock();

 double tiempo = (double)(fin - inicio)/CLOCKS_PER_SEC;

 printf("Fibonacci(%d) = %ld\n", n, resultado);
 printf("Tiempo en C: %f segundos\n", tiempo);

 return 0;
}
