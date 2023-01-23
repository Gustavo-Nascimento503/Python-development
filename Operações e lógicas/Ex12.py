h = int (input('Digite o valor da altura: '))
b = int (input('digite o valor da base: '))

area = b * h 

print('seu resultado e: ', area)

if area > 100:
    print('terreno muito grande')
else:
    print('terreno pequeno')