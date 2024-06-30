peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / altura ** 2

print('Seu imc é {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 < 25:
    print('Peso ideal')
elif imc <= 25 < 30:
    print('Sobrepeso')
elif imc <= 30 < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade mórbida')