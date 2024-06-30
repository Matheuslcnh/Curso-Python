import math
nome = input('Digite seu nome: ').upper().strip()
print('A letra A aparece {} vezes'.format((nome.count('A'))))
print('A 1° letra A aparece na posição {}'.format(nome.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(nome.rfind('A')+1))
