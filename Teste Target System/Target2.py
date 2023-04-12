def verificaFibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n:
        return True
    else:
        return False

numero = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))

if verificaFibonacci(numero):
    print(numero, "pertence à sequência de Fibonacci.")
else:
    print(numero, "não pertence à sequência de Fibonacci.")