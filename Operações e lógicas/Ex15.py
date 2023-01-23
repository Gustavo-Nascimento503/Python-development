l1 = int(input('digite o lado 1'))
l2 = int(input('digite o lado 2: '))
l3 = int(input('digite o lado 3: '))

if (l1 + l2) > l3 and (l1 + l3) > l2 and (l3 + l2) >l1:

    if (l1 == l2) and (l1 == l3):
        print('equilatero')

    elif (l1 !=  l3) and (l1 != l2) and (l2 != l3):
        print ('Escaleno')

    else:
        print('isoceles')
else:
    print('nao e um triangulo')