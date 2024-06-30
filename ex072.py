n = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez' )
usu = int(input('Digite um numero de 0 a 10: '))
while usu < 0 or usu > 10:
    usu = int(input('Seu numero esta errado. Digite novamente: '))
print(f'Você digitou o número {n[usu]}')