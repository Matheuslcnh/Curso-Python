import random
'''
aluno = random.randint(1, 4)
print(aluno)
if aluno == 1:
    print('O nome escolhido é Matheus' )
elif aluno == 2:
    print('O nome escolhido é Pedro' )
elif aluno == 3:
    print('O nome escolhido é Davi' )
elif aluno == 4:
    print('O nome escolhido é Gustavo' )
    '''
#ou

n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')

lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhino foi {}'.format(escolhido))


