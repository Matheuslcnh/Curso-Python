dias = float(input('Quantas dias voce alugou: '))
km = float(input('Quantos km voce rodou: '))
preco = (dias * 60) + (0.15 * km)
print(f'o total a pagar é R${preco}')
