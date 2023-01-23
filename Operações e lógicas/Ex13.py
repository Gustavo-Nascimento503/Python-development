v1 = int(input('digite o primeiro valor: '))
v2 = int(input('digite o segundo valor: '))
v3 = int(input('digite o terceiro valor: '))

maiorNum = v1

if(v2 > v1 and v2 > v3):
    maiorNum = v2
    print(maiorNum)
elif(v3 > v1 and v3 > v2):
    maiorNum = v3
    print('o terceiro e o maior: ', maiorNum)
else:
    print(maiorNum)