menu = input("1 triangulo,  2 quadrado, 3 retangulo, 4 circulo, 5 fim do processo")

if(menu == "1"):
    b = int(input("DIgite o valor da base"))
    h = int(("digite o valor da altura"))
    triangulo = b * h / 2
    
    print("triangulo = ", triangulo)
elif(menu == "2"):
    lado = int(input("digite o valor do lado do quadrdado: "))
    quadrado = lado * lado

    print("quadrado = ", quadrado)
elif(menu == "3"):
    b = int(input("DIgite o valor da base"))
    h = int(("digite o valor da altura"))
    retangulo = b * h
    
    print("retangulo = ", retangulo)
elif(menu == "4"):
    raio = float(input("Digite o valor do raio: "))
    circulo = raio * 3.14

    print("circulo = ", circulo)
elif(menu == "5"):
    print("processo encerrado")
    exit()
else:
    print("invalido")