import time

def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


n = 35

inicio = time.time()

resultado = fibonacci(n)

fin = time.time()

print("Fibonacci(",n,") =",resultado)
print("Tiempo en Python:", fin-inicio,"segundos")
