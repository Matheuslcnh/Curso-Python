

from uteis.calculos import moeda
p = int(input('Digite o preço: R$ '))

print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'o dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumento 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')