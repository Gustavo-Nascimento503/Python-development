p1 = int(input('Digite o numero da primeira nota: '))
p2 = int(input('digite o valor da segunda nota'))
media = (p1 + (p2 * 2)) / 3

if(media > 5):
    print('aprovado')
else:
    print('reprovado')
