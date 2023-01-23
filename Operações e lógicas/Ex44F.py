soma = 0

for i in range(1, 11, 1):
    numero = int(input('digite um numero: '))
    while(numero<0):
        print('numero negativo digite novamente: ')
        numero = int(input('digite um numero: '))


    if(i == 1):
        maior = numero
    elif(numero > maior):
        maior = numero

    
    soma = soma + numero

    
media = soma / 10

print('o maior é: ', maior)
print('soma é: ', soma)
print('a media é: ', media)