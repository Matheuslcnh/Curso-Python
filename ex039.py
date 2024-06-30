'''
ano = int(input('Informe sua idade: '))
if ano < 18:
    print('Você ainda vai se alistar!')
    print('Falta {} anos'.format(18 - ano))
elif ano == 18:
    print('esta na hora de se alistar')
elif ano > 18:
    print('Ja passou da hora de alistar!!')
    print('Era para ter se alistado faz {} anos'.format(ano - 18))
    '''
    #ou

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade,atual))
if idade == 18:
    print('Você tem que se alistar imediatamente: ')
elif idade < 18:
    saldo = idade - 18
    print('Voce ainda nao tem 18 anos, ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado ha {} anos'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento foi em {}'.format(ano))