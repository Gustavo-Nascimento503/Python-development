x = int(input('digite o valor de X: '))

while(x < 0):
    print('o valor tem que ser negativo, digite a baixo ')
    x = int(input('digite o valor de X: '))

a = int(input('digite o inicio do intervalo: '))
b = int(input('digite o fim do intervalo: '))

while(b <= a):
    print('digite o valor de b novamente: ')
    b = int(input('digite o fim do intervalo: '))


while(b >= a):
    t = x * b
    print(t, 'x', b, '=', t)
    b = b - 1