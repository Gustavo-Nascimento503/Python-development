nome = []
idade = []
sexo = []

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

for i in range(0, 5, 1):
    if(sexo[i] == 'f'):
        print("Seu nome é: ", nome[i])
        print("Sua idade é: ", idade[i])
        print("Seu sexo é: ", sexo[i])
    


