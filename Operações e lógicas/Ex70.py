matriz = [[]]


linhas = int(input('Digite a quantidade de linhas que a matriz terá: '))
colunas = int(input('Digite a quantidade de colunas que a matriz terá: '))

while(linhas > 10 and colunas > 10):
    print('digite novamente')
    linhas = int(input('Digite a quantidade de linhas que a matriz terá: '))
    colunas = int(input('Digite a quantidade de colunas que a matriz terá: '))
 

for i in range(0, linhas, 1):
    matriz.append([])

for l in range(0, linhas, 1):
    for c in range(0, colunas, 1):    
        num = int(input('Digite um numero: '))
        matriz[l].append(num)

verificar = int(input('digite a posição: '))

res = ""
for l in range(0, linhas, 1):
    for c in range(0, colunas, 1):
        if(matriz[l][c] == verificar):    
            res = res + "[" + str(l) + ", " + str(c) + "] "

if (res == ""):
    print('O numero nao foi encontrado na matriz')
else:
    print(res)



pergunta = "s"

while(pergunta == "s"):
    verificar = int(input('digite a posição: '))

    res = ""
    for l in range(0, linhas, 1):
        for c in range(0, colunas, 1):
            if(matriz[l][c] == verificar):    
                res = res + "[" + str(l) + ", " + str(c) + "] "

    if (res == ""):
        print('O numero nao foi encontrado na matriz')
    else:
        print(res)
