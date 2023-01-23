
n = int(input('digite o valor de n: '))

while(n <0 or n>100):
    print('o valor de n deve ser positivo: ')
    n = int(input('digite o valor de n: '))

for i in range(0,n,1):
    if(i==0):
        a=((i + 1)*(i +1 )) +1
    else:
        a = a +((i + 1)*(i + 1))+1
        print(a)




