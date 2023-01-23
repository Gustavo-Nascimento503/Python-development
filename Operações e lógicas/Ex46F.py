
soma = 0

for i in range(1, 5, 1):
    numero = int(input('digite um numero: '))

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

decisao = input('digite s para repetir e n para encerrar')

if(decisao == 's'):
    for i in range(1, 5, 1):
        numero = int(input('digite um numero: '))

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

else:
    print('encerrado')