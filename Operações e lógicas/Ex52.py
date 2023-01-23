numeros = []
maior = 0
for i in range(1, 11, 1):
    numeros.append(int(input('Digite um numero: ')))

for i in range(0, 10, 1):
    if (numeros[0] < numeros[i]):
        numeros[0] = numeros[i]

print(numeros[0])
