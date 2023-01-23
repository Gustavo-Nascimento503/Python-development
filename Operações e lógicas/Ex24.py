nome = input('digite seu nome: ')
sexo = input('m/f: ')
estado_civil = input("solteira ou casada: ")

if sexo == "f" and estado_civil == "casada":
    print("digite so tempo de casada em anos abaixo: ")
    tempo_casado = int(input("digite o tempo: "))

elif sexo == "m":
    print("seu sexo nao é feminino")

else:
    print("invalido")
