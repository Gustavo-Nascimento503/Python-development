n = int(input("digite o valor: "))

while (n <= 0) or (n > 50):
    n = int(input("O valor da sequência de termos deve ser positivo e menor que cinquenta. Informe novamente: "))

numerador = 1
denominador = 2
soma = 0

for i in range(1, n, 1):
    numerador = (i ** 2) + 1
    denominador = (i ** 3)
    divisao = numerador / denominador
    if (i == 1): print(f'{numerador}')
    else: print(f"{numerador}/{denominador}")
    soma = soma + divisao

print('A soma é: %.2f' %soma)