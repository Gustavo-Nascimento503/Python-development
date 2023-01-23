matriz = [[]]
matriz_2 = [[]]

linhas = int(input('Digite a quantidade de linhas que a matriz terá: '))
colunas = int(input('Digite a quantidade de colunas que a matriz terá: '))
 
# Cria as linhas na Matriz
for i in range(0, linhas, 1):
    matriz.append([])

for l in range(0, linhas, 1):
    for c in range(0, colunas, 1):    
        num = int(input('Digite um numero: '))
        matriz[l].append(num)



const = int(input('digite o multipicador: '))

for l in range(0,linhas, 1):
    for c in range(0, colunas, 1):
     matriz[l][c] = matriz_2[l][c] * const

for i in range(0, 3, 1):
    print(matriz[l])

for i in range(0, 3, 1):
    print(matriz_2[l])