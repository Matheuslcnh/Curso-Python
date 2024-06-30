contador = 0
soma = 0
n = 0
n = int(input('Digite um numero [para parar 999]: '))
while n != 999:
    contador += 1
    soma += n
    n = int(input('Digite um numero [para parar 999]: '))
print('Você digitou {} numeros e a soma entre eles foi {} '.format(contador, soma))

    
