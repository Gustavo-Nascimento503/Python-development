nome = []
idade = []
sexo = []

for i in range(0, 3, 1):
    n = (input("digite seu nome: "))
    nome.append(n)

    id = int(input("digite sua idade: "))
    idade.append(id)

    sex = (input("digite seu sexo em m/f: "))
    sexo.append(sex)

for i in range(0, 3, 1):
    for j in range(i+1, 3, 1):
        if(idade[i] < idade[j]):
            maior = idade[i]
            ant = idade[j]
            idade[j] = maior
            idade[i] = ant

print(idade, nome, sexo)
