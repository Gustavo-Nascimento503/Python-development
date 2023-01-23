n = int(input("Qual é o valor de N:"))

while (n <= 0 or n > 50):
    n = int(input("O valor da sequência de termos deve ser positivo e menor que cinquenta. Informe novamente: "))

numerador = 1
denominador = 2
i = 1
soma = 0

while (i < n):
    divisior = numerador / denominador
    soma = soma + divisior
    print(f"{i}. {numerador}/{denominador}")
    numerador = numerador + 1
    denominador = denominador + 1
    i = i + 1

print("A soma deu: %.2f" % soma)