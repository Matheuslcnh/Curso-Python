'''from math import factorial
n = int(input('Digite um numero: '))
fatorial = factorial(n)
print('o fatorial de {} é {}'.format(n, fatorial))'''

n = int(input('Digite um numero: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x 'if c > 1 else '=', end='')
    f = f * c
    c -= 1
print(' {} '.format(f))

