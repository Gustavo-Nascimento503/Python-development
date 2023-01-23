
soma = 0
i = 1

while(i <= 5):
    numero = int(input('digite um numero POSITIVO: '))

    if(i == 1):
        maior = numero
        i = i + 1
    elif(numero > maior):
        maior = numero
        i = i + 1
    if(i == 1):
        menor = numero
        i = i + 1
    elif(numero < menor):
        menor = numero
        i = i + 1

    
    soma = soma + numero

media = soma / 4

porcentagem = soma * 0.1

print(maior)
print(menor)
print(soma)
print(media)
print(porcentagem)

