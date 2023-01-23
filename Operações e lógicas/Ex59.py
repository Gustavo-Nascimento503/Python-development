nome = []
idade = []
sexo = []
l = 0

for i in range(0, 5, 1):
    n = (input("digite seu nome: "))
    nome.append(n)
    

    id = int(input("digite sua idade: "))
   
    while(id < 0):
     id = int(input("digite sua idade: "))
    
    idade.append(id)


    sex = (input("digite seu sexo em m/f: "))
    
    while(sex != 'f' and sex != 'm'):
        sex = (input("digite seu sexo em m/f: "))

    sexo.append(sex)



for i in range(0, 2, 1):
    if(idade[i] >= 18):
        confirma = (input("pressione enter para mostrar: "))
        print(confirma)
        print("Seu nome é: ", nome[i])
        print("Sua idade é: ", idade[i])
        print("Seu sexo é: ", sexo[i])
        l = l + 1
print('numero de pessoas maior que 18 anos: ', l)

for i in range(3, 5, 1):
    if(idade[i] >= 18):
        confirma = (input("pressione enter para mostrar: "))
        print(confirma)
        print("Seu nome é: ", nome[i])
        print("Sua idade é: ", idade[i])
        print("Seu sexo é: ", sexo[i])
        l = l + 1
print('numero de pessoas maior que 18 anos: ', l)