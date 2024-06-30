casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salario: '))
anos = int(input('Quantos anos você vai pagar: '))
minimo = salario * 30 / 100
mes = anos * 12
valor = casa / mes
print('meses: {:.0f}'.format(mes))
print(f'o valor por mes é R${valor :.2f}')

if valor <= minimo:
    print('Emprestimo pode ser concebido')
else:
    print('Negado')

