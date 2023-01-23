altura = float(input('digite a altura: '))
peso = float(input('digite a peso'))

imc = peso / (altura * altura)

if imc > 50:
    print('voce esta no peso ideal')
elif imc <= 50:
    print('seu peso nao esta ideal')
