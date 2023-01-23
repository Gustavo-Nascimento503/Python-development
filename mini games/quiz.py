print("Seja bem vindo a o meu quiz!")

answer_user = input("Deseja começar? (S/N)")


if answer_user != "S":
    quit()

score = 0

print("Iniciando...")
print("Quem fundou a Google? \n (A) Larry Page e Sergey Brin \n (B) Sam Houser e Dan Houser \n (C) Richard McDonald e Maurice McDonald \n (D) Bruno e Marrone")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Correto!!")
    score = score + 1
else:
    print("Incorreto!!")

print("O que significa a sigla “www” na internet? \n (A) Web world wide \n (B) World wide web (C) Web wide world \n (D) Web World Web")
answer_2 = input("Resposta: ")

if answer_2 == "B":
    print("Correto!!")
    score = score + 1
else:
    print("Incorreto!!")

print(f"Quiz encerrado... Pontuação: {score}/2")


