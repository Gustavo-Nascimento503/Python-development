p1 = float(input('Digite o numero da primeira nota: '))
p2 = 7.5 - p1 / 2
media = (p1 + (p2 * 2)) / 3



if(media > 5):
    print("aprovado")
else:
    print("voce precisa de: ", media)