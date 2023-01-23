num = []

novamente = 's'

qtd = int(input('digite a quantidade de valores a serem digitados: '))

while(qtd <= 0 or qtd > 20):
    print('apenas numeros até que 20')
    qtd = int(input('digite a quantidade de valores a serem digitados: '))

for i in range(0, qtd, 1):
    x = int(input('digite um valor: '))
    num.append(x)

while(novamente == 's'):
    numero = int(input('digite o numero a ser localizado no array'))
    pos = -1
    for i in range(0, qtd, 1):
        if(num[i] == numero):
            pos = i

    if (pos != -1):
        print('o valor foi encontrado na posiçao: ', pos)
    else:
        print('valor não encontrado.')

    novamente = input('deseja realzar nova consulta? s/n')        
