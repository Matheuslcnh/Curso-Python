from uteis.calculos import moeda
from uteis.dado import dados

p = dados.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 40)