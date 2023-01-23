produto = float(input('digite o valor do produto: '))
forma_pgto = input('1- Dinheiro ou cheque, 2- cartão, 3- em duas vezes, 4- em 4 vezes: ')

if(forma_pgto == '1'):
    produto_desconto = produto -(0.10 * produto)
    print('seu desconto é de 10%: ', produto = produto_desconto)
elif(forma_pgto == '2'):
    produto_desconto = produto - (0.15 * produto)
    print('seu desconto é de 15% ', produto * 0.15, produto)
elif(forma_pgto == '3'):
    print('2 vezes sera em preço normal: ',produto / 2)
else:
    print('em 4 vezes preço normal com juros de 10%: ', produto / 4 * 0.10)