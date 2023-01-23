numeros = []
resultado = []

for i in range(0, 21, 1):
    num = int(input('digite o valor: '))
    numeros.append(num)

const = int(input('digite o valor da constatante: '))

for i in range(0, 21, 1):
    resultado.append(const * numeros[i])
    print(numeros[i])


print('Os vetores são: ')
for i in range(0, 5, 1):
    print(resultado[i])