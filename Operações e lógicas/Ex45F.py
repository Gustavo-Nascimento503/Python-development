
soma = 0

for i in range(1, 6, 1):
    numero = int(input('digite um numero POSITIVO: '))

    if(i == 1):
        maior = numero
    elif(numero > maior):
        maior = numero
    if(i == 1):
        menor = numero
    elif(numero < menor):
        menor = numero

    
    soma = soma + numero

media = soma / 4

porcentagem = soma * 0.1

print(maior)
print(menor)
print(soma)
print(media)
print(porcentagem)

