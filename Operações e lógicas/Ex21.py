v1 = int(input("digite o valor:"))
v2 = int(input("digite o outro valor:"))


menu = input("1 para somar, 2 para multiplicar, 3 para dividir, 4 para subtrair, 5 para finalizar ")


if (menu == "1"):
    resultado = (v1 + v2)
    print("soma é", resultado)
elif(menu == "2"):
    resultado = v1 * v2
    print(resultado)
elif(menu == "3"):
    resultado = v1 / v2
    print(resultado)
elif(menu == "4"):
    resultado = v1 - v2
    print(resultado)
elif(menu == "5"):
    print("o programa encerrou")
    exit()
else:
    print("invalido")