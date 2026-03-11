Punto 1 – AFD para movimientos de ajedrez
Este programa implementa un Autómata Finito Determinista (AFD) que reconoce un lenguaje de movimientos simplificados de ajedrez..
La estructura general del lenguaje es:
[pieza] -> [pieza][posición]
o captura:
[pieza]X[pieza]
Ejemplos válidos:
p->k4
kbpXqn
abc->d2
Ejemplos inválidos:
4abc
p-k4
El programa utiliza Python y expresiones regulares para simular el comportamiento del AFD.

Punto 2 – Implementación de un AFD para Identificadores en Python
1. Introducción
En este ejercicio se implementa un Autómata Finito Determinista (AFD) utilizando Python para reconocer identificadores válidos según la expresión regular:
[A-Za-z][A-Za-z0-9]*
Un identificador es una cadena utilizada para nombrar variables, funciones u otros elementos en un lenguaje de programación. Para que un identificador sea válido debe cumplir ciertas reglas definidas por la expresión regular anterior.
El programa analiza una cadena de caracteres y determina si esta pertenece o no al lenguaje definido por la expresión regular.
2. Expresión Regular
La expresión regular utilizada es:
[A-Za-z][A-Za-z0-9]*


Significado
Parte	Descripción
[A-Za-z]	El primer carácter debe ser una letra mayúscula o minúscula
[A-Za-z0-9]	Los siguientes caracteres pueden ser letras o números
*	Significa que puede haber cero o más caracteres después del primero
	
	
Ejemplos válidos:
Juan
abc123
Variable9
X

Ejemplos inválidos:
9variable
@nombre
123abc
3. Diseño del Autómata Finito Determinista (AFD)
El AFD se define mediante un conjunto de estados y transiciones.
Estados
Estado	Descripción
q0	Estado inicial
q1	Estado de aceptación
q_dead	Estado de rechazo
	
	



	

Transiciones del AFD
Estado actual	Entrada	Estado siguiente
q0	letra	q1
q0	otro símbolo	q_dead
q1	letra	q1
q1	número	q1
q1	otro símbolo	q_dead

Estado de aceptación
El estado de aceptación es:
q1
Si al terminar de leer la cadena el autómata se encuentra en este estado, la cadena es aceptada.
4. Pruebas del programa
Para verificar el funcionamiento del programa se creó el archivo:
pruebas2.txt
Contenido del archivo:
Juan
abc123
Variable9
9abc
@nombre






Resultados esperados:
Entrada	Resultado
Juan	ACEPTA
abc123	ACEPTA
Variable9	ACEPTA
9abc	NO ACEPTA
@nombre	NO ACEPTA

5. Ejecución del programa
Para ejecutar el programa:
python punto2_afd_identificador.py
El programa leerá las cadenas del archivo pruebas2.txt y mostrará si cada una es aceptada o rechazada por el autómata.
6. Conclusión
El programa implementa correctamente un Autómata Finito Determinista para validar identificadores basados en la expresión regular especificada.
El uso de Python permite simular fácilmente las transiciones entre estados y verificar si una cadena pertenece al lenguaje definido.


Punto 3 – Calculadora de Raíz Cuadrada usando Flex, Bison y C
1. Introducción
En este ejercicio se implementa una calculadora en lenguaje C que permite calcular la raíz cuadrada de números reales utilizando el método numérico Newton-Raphson.
Para construir el programa se utilizan las herramientas:
	Flex: para el análisis léxico.
	Bison: para el análisis sintáctico.
	C: para implementar la lógica del cálculo.
El programa lee instrucciones desde un archivo de texto y muestra los resultados en la consola.
2. Método Newton-Raphson
El método Newton-Raphson es un algoritmo iterativo utilizado para encontrar aproximaciones de raíces de funciones.
Para calcular la raíz cuadrada de un número Sse utiliza la fórmula:
x_(n+1)=1/2 (x_nⓜ+S/x_n )

donde:
	Ses el número del cual se desea calcular la raíz.
	x_nes la aproximación actual.
	x_(n+1)es la siguiente aproximación.
El proceso se repite hasta que la diferencia entre aproximaciones sea muy pequeña.
Por ejemplo, para calcular √25:
Iteración	Valor aproximado
x₀	25
x₁	13
x₂	7.46
x₃	5.40
x₄	5.01
x₅	5.00

Finalmente se obtiene el valor aproximado 5
3. Herramientas utilizadas
El programa se desarrolló utilizando herramientas disponibles en Ubuntu.
Flex
Flex es un generador de analizadores léxicos. Se encarga de identificar los tokens del lenguaje.
En este programa Flex reconoce:
	la palabra clave sqrt
	números reales
	saltos de línea

Bison
Bison es un generador de analizadores sintácticos que trabaja junto con Flex.
Bison define la gramática del lenguaje y determina cuándo ejecutar las operaciones.
En este caso, cuando se detecta la estructura:
sqrt numero
se ejecuta la función que calcula la raíz cuadrada.
4.  Implementación del método Newton-Raphson
La función que calcula la raíz cuadrada es:
double newton(double n)
Proceso del algoritmo:
	Se toma una aproximación inicial.
	Se aplica la fórmula de Newton-Raphson.
	Se repite hasta que la diferencia entre iteraciones sea menor que un error definido.
	Se retorna la raíz calculada.
El error usado en el programa es:
0.00001
Esto garantiza una buena precisión:

	Archivo de entrada
El programa lee las instrucciones desde el archivo:
input.txt
Contenido del archivo:
sqrt 25
sqrt 2
sqrt 144
sqrt 10
Cada línea representa una operación que el programa debe calcular.

	Compilación del programa
Para compilar el programa se deben ejecutar los siguientes comandos en la terminal.
Generar el parser
bison -d calc.y
Generar el lexer
flex calc.l
Compilar el programa
gcc calc.tab.c lex.yy.c -o calculadora -lfl

	Ejecución del programa
Para ejecutar el programa utilizando el archivo de entrada:
./calculadora < input.txt

Resultados obtenidos
Salida del programa:
Calculadora de raiz cuadrada (Newton-Raphson)
Resultado: 5.000000
Resultado: 1.414214
Resultado: 12.000000
Resultado: 3.162277

Conclusión
Se desarrolló una calculadora capaz de interpretar instrucciones para calcular raíces cuadradas utilizando Flex, Bison y C.
El programa utiliza el método numérico Newton-Raphson, que permite obtener aproximaciones precisas de raíces cuadradas mediante iteraciones sucesivas.
El uso de Flex y Bison facilita la construcción de lenguajes y procesadores de instrucciones, permitiendo separar claramente el análisis léxico, el análisis sintáctico y la lógica del cálculo.


Punto 4– Comparación de rendimiento entre C y Python
1. Objetivo
Comparar el tiempo de ejecución de una función recursiva implementada en dos lenguajes:
	C (compilado)
	Python (interpretado)
La comparación se realiza calculando la secuencia de Fibonacci.
2. Función recursiva utilizada
La función de Fibonacci se define como:
F(n)=F(n-1)+F(n-2)

con condiciones iniciales:
F(0)=0
F(1)=1

Ejemplo:
n	Fibonacci
0	0
1	1
2	1
3	2
4	3
5	5
6	8


3. Compilación del programa en C
En Ubuntu se compila así:
gcc fibonacci_c.c -o fib_c
Ejecutar:
./fib_c
4. Ejecutar el programa en Python
python3 fibonacci_python.py
5. Resultados
 
6. Explicación de la diferencia de rendimiento
La diferencia de rendimiento se debe a que:
Lenguaje compilado (C)
	El código se traduce directamente a código máquina
	El procesador lo ejecuta directamente
	Mayor velocidad
Lenguaje interpretado (Python)
	El código es ejecutado por un intérprete
	Cada instrucción se analiza durante la ejecución
	Mayor consumo de tiempo

7. Conclusión
Los resultados muestran que el lenguaje compilado C ejecuta la función recursiva significativamente más rápido que Python.
Esto ocurre porque los lenguajes compilados generan código optimizado para la arquitectura del sistema, mientras que los lenguajes interpretados requieren un proceso adicional de interpretación durante la ejecución.
Sin embargo, Python ofrece ventajas como:
	mayor facilidad de programación
	menor tiempo de desarrollo
	código más legible


Punto 5 – Implementación de Fibonacci usando ANTLR
1. Introducción
En este punto se implementa un pequeño intérprete capaz de reconocer una instrucción del tipo:
FIBO(n)
donde n es un número entero.
El programa interpreta la instrucción y muestra en consola la secuencia de Fibonacci hasta el número indicado.
Para realizar el análisis sintáctico se utiliza ANTLR, una herramienta que permite generar analizadores léxicos y sintácticos a partir de una gramática definida.
El lenguaje objetivo utilizado para ejecutar el programa es Python.
2. Herramientas utilizadas
	ANTLR para generar el lexer y parser.
	Python para implementar la lógica del programa.
	Terminal de Ubuntu para ejecutar los comandos.

3. Gramática del lenguaje
Se define una gramática sencilla capaz de reconocer la instrucción FIBO(n).
Archivo:
fibonacci.g4
Contenido:
grammar fibonacci;

prog: 'FIBO' '(' NUMBER ')' EOF;

NUMBER: [0-9]+;

WS: [ \t\r\n]+ -> skip;
Explicación
	prog: regla principal que reconoce la instrucción completa.
	NUMBER: token que representa números enteros.
	WS: ignora espacios en blanco.

4. Generación del parser
Una vez definida la gramática, se utiliza ANTLR para generar los archivos necesarios para Python.
Comando ejecutado en la terminal:
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 fibonacci.g4
Este comando genera automáticamente los archivos:
fibonacciLexer.py
fibonacciParser.py
fibonacciListener.py
Estos archivos contienen el lexer y parser necesarios para analizar la entrada del usuario.
5. Implementación en Python
Se crea un programa en Python que utiliza el parser generado para procesar la entrada.
Archivo:
Fibo_main.py
Código:
from antlr4 import *
from fibonacciLexer import fibonacciLexer
from fibonacciParser import fibonacciParser

def fibonacci(n):

    a, b = 0, 1
    seq = []

    for i in range(n):
        seq.append(a)
        a, b = b, a + b

    return seq


def main():

    entrada = input("Ingrese instrucción: ")

    input_stream = InputStream(entrada)
    lexer = fibonacciLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = fibonacciParser(stream)

    parser.prog()

    numero = int(entrada.split("(")[1].split(")")[0])

    resultado = fibonacci(numero)

    print("Secuencia Fibonacci:")
    print(resultado)


if __name__ == "__main__":
    main()

6. Ejecución del programa
Para ejecutar el programa primero se debe instalar el runtime de ANTLR para Python:
pip install antlr4-python3-runtime
Luego ejecutar el programa:
python3 fibo_main.py
Ejemplo de entrada:
FIBO(8)
Salida generada:
Secuencia Fibonacci:
[0, 1, 1, 2, 3, 5, 8, 13]

7. Conclusión
Se implementó un pequeño intérprete capaz de reconocer instrucciones de la forma FIBO(n) utilizando ANTLR para el análisis sintáctico y Python para la ejecución del programa. El sistema valida la estructura de la instrucción y posteriormente calcula la secuencia de Fibonacci correspondiente, mostrando el resultado por consola.
