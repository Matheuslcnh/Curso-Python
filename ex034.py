salario = float(input('Digite seu salario: '))
a1 = salario * (10/100)
a2 = salario * (15/100)
if salario > 1250:
    print('Seu aumento é 10%, portanto R${}'.format(salario * (10/100)))
    print('totalizando fica R${:.2f}'.format(salario + a1))
else:
    print('Seu aumento é de 15%, portanto R${}'.format(salario * (15/100)))
    print('totalizando fica R${:.2f}'.format(salario + a2))