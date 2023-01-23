import random

userPoints = 0
computerPoints = 0

options = ["r", "t", "p"]

while True:
    userChoice = input("Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair.").lower()

    if userChoice == 'q':
        break

    if userChoice not in options:
        continue

    computerChoice = random.randint(0, 2)
    # 0 : R, 1: T, 2: P
    computerOptions = options[computerChoice]

    print("O computador escolheu: " + computerOptions)

    if userChoice == computerOptions:
        print("Empate")
    
    elif userChoice == "r" and computerOptions == "t":
        print("Você ganhou!")
        userPoints = userPoints + 1
    
    elif userChoice == "p" and computerOptions == "r":
        print("Você ganhou!")
        userPoints = userPoints + 1
    
    elif userChoice == "t" and computerOptions == "p":
        print("Você ganhou!")
        userPoints = userPoints + 1
    else:
        print("Você perdeu")
        computerPoints = computerPoints + 1

print("Sua pontuação: " + str(userPoints))
print("pontuação do computador: " + str(computerPoints))

if computerPoints > userPoints:
    print("Derrota!!!")
elif computerPoints ==  userPoints:
    print("Empate!!!")
else:
    print("Vitória!!!")



print("Encerrando...")
