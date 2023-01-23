numeros = []
valor = []
ordem = []

for i in range(0, 5, 1):
    numeros.append(int(input('Digite um numero: ')))
    if numeros < valor:
        ordem.append(numeros)
print(ordem)

