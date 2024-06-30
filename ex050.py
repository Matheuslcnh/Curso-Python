soma = 0 
for n in range(6):
    n = int(input('Numero: '))
    if n % 2 == 0:
        soma += n
print('A soma dos números pares são {}'.format(soma))