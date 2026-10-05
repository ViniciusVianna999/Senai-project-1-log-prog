def fatorial(numero):
    if numero == 0:
        return 1
    return numero * fatorial(numero - 1)

print(fatorial(5))  # Output: 120

def fibonacci(numero):
    if numero <= 0:
        return numero
    return fibonacci(numero - 1) + fibonacci(numero - 2)

print(fibonacci(10))  