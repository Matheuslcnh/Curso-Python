dis = float(input('Digite a distancia: '))
if dis <= 200:
    print('O preço será R${:.2f}'.format(dis * 0.50))
else:
    print('O preço será R${:.2f}'.format(dis * 0.45))