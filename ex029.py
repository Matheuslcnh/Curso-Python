v = float(input('Qual é a velocidade do carro: '))
if v > 80:
    print('Voce foi multado')
    print('A multa será {} reais'.format((v - 80)*7 ))
else: 
    print('Esta tudo ok')