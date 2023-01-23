v1 = 0
v2 = 1
soma = 1

for i in range(0,31):
    print('soma = ', v1)
    soma = v2 + v1
    v1 = v2
    v2 = soma