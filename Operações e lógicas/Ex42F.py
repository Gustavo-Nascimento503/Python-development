n = int(input("digite o valor: "))

while (n <= 0 or n > 50):
    n = int(input("O valor da sequência de termos deve ser positivo e menor que cinquenta. Informe novamente: "))

numerador = 1
denominador = 2
soma = 0

for i in range(1, n, 1):
    divisor = numerador / denominador
    soma = soma + divisor
    print(f"{i}. {numerador}/{denominador}")
    numerador = numerador + 1
    denominador = denominador + 1

print("A soma deu: %.2f" % soma)