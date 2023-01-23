n = int(input('digite o valor de n: '))

while(n <0 or n>100):
    print('o valor de n deve ser positivo: ')
    n = int(input('digite o valor de n: '))

i = 0

while(i <= n):
    if(i == 0):
        a=((i + 1)*(i +1 )) +1
        i = i + 1 
    else:
        a = a +((i + 1)*(i + 1))+1
        i = i + 1
        print(a)