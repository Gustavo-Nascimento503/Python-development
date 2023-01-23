a = float(input("Digite o valor da aceleração (em m/s2): "))

v0 = float(input('Digite o valor da velocidade inicial (em m/s): '))

t = float(input("Digite o valor do tempo de percurso (t em s): "))

v = v0 + (a * t)

if (v <=40):
    print('Veiculo muito lento, a velocidade é:', v)
elif (v <= 60):
    print('Velocidade permitida, a velocidade é:', v)
elif (v <= 80):
    print('Velocidade de cruzeiro, a velocidade é:', v)
elif (v <= 120):
    print('Veiculo muito rápido, a velocidade é:', v)
else:
    print('Veiculo muito rápido, a velocidade é:', v)