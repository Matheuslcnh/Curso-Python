'''
n = int(input('Digite o numero: '))
print(f'Tabuada do numero {n}:')
print(f'{n * 1}\n{n * 2}\n{n * 3}\n{n * 4}\n{n * 5}\n{n * 6}\n{n * 7}\n{n * 8}\n{n * 9}\n{n * 10}')
'''



#exercicio 49

n = int(input('Digite um numero da tabuada que voce quer: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))