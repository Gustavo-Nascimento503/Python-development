numeros = []
vetor = []
for i in range(0, 20, 1):
    numeros.append(int(input('digite os umeros: ')))
    indice = indice + 1

    if(i == 0):
        menor = vetor[i]

    else:
        for j in range(0, 20, 1):
            if(vetor[i] < vetor[j]):
                menor = vetor[i]
                prox = vetor[j]
                vetor[j] = menor
                vetor[i] = prox
print(vetor)