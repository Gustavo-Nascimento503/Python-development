
string = input("Digite uma palavra: ")


caracteres = list(string)


meio = len(caracteres) // 2


for i in range(meio):
    
    oposto = len(caracteres) - i - 1
    caracteres[i], caracteres[oposto] = caracteres[oposto], caracteres[i]

stringInvertida = "".join(caracteres)


print(stringInvertida)
