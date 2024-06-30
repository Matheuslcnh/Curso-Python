import random
from time import sleep
'''
n = random.randint(0, 5)

usuario = int(input('Digite um numero de 0 a 5: '))
print('PROCESSANDO......')
sleep(3)
if usuario == n:
    print('Voce é brabooo')
else: 
    print('Voce é horrivel')'''
    
n = random.randint(1, 10)
print(n)
contador = 0
while True:
    usuario = int(input('Valor: '))
    if usuario != n:
        print('não')
        contador += 1
    else:
        print('Acertou')
        print('Você acertou em {} tentativas'.format(contador))
        break
    

    
