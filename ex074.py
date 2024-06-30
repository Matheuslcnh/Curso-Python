from random import randint
nu = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for n in nu:
    print(n, end=' ')
print(f'\nO maior valor sorteado foi {max(nu)}')
print(f'O menor valor sorteado foi {min(nu)}')

