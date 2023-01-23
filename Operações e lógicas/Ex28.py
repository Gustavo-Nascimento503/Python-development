v1 = float(input('digite o primeiro valor: '))
v2 = float(input('digite o segundo valor: '))
v3 = float(input('digite o terceiro valor: '))

if (v1 > v2 > v3):
    print(v1, v2, v3)

elif(v1 > v3 > v2):
    print(v1, v3, v2)

elif(v2 > v1 > v3):
    print(v2, v1, v3)

elif(v2 > v3 > v1):
    print(v2, v3, v1)

elif(v3 > v1 > v2):
    print(v3, v1, v2)
else:
    print(v3, v2, v1)