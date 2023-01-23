numeros = []

for i in range(0, 10, 1):
    numeros.append(int(input('Digite um numero: ')))
 
print('Os numeros que você digitou foram: ')

#append criar posiçao
 

for i in range(9, -1, -1):
    print(numeros[i])