n = int(input("digite o valor"))

while (n <= 0) or (n > 50):
    n = int(input("O valor da sequência de termos deve ser positivo e menor que cinquenta. Informe novamente: "))

numerador = 1
denominador = 2
i = 1
soma = 0

while (i < n):
    numerador = (i ** 2) + 1
    denominador = (i ** 3)
    divisao = numerador / denominador
    if (i == 1): print(f'{numerador}')
    else: print(f"{numerador}/{denominador}")
    i = i + 1
    soma = soma + divisao

print('A soma é: %.2f' %soma)