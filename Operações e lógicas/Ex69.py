matriz = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
matriz_2 = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]

for l in range(0, 3, 1):
    for c in range(0, 4, 1):
        matriz[l][c] = int(input('Digite um numero: '))

const = int(input('digite o multipicador: '))

for i in range(0,3, 1):
    for j in range(0, 4, 1):
     matriz[l][c] = matriz_2[l][c] * const

for i in range(0, 3, 1):
    print(matriz[l])

for i in range(0, 3, 1):
    print(matriz_2[l])