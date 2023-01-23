peso = float (input('digite o peso: '))
altura = float (input('digite a altura: '))
Sexo = input("Insira o seu sexo (m/f): ")

# masculino

imc = peso / (altura * altura)

if (Sexo == 'm'):
    if (imc < 20):
        print('voce esta abaixo do peso')
    elif imc < 25:
        print('ideal')
    else:
        print('acima do peso')

# feminino

else: 
    (Sexo == 'f')
    if (imc < 19):
        print('voce esta abaixo do peso')
    elif imc < 24:
        print('ideal')
    else:
        print('acima do peso')
