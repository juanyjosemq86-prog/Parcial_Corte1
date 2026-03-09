from antlr4 import *
from FibonacciLexer import FibonacciLexer
from FibonacciParser import FibonacciParser

def fibonacci(n):
    seq = []
    a, b = 0, 1

    for i in range(n):
        seq.append(a)
        a, b = b, a + b

    return seq


def main():

    entrada = input("Ingrese comando: ")

    input_stream = InputStream(entrada)
    lexer = FibonacciLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FibonacciParser(stream)

    tree = parser.expr()

    texto = entrada.replace("FIBO(", "").replace(")", "")
    n = int(texto)

    resultado = fibonacci(n)

    print("Secuencia Fibonacci:")
    print(resultado)


if __name__ == '__main__':
    main()
