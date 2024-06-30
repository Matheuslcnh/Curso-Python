'''nome = input('Nome: ')
media = float(input(f'Media de {nome}: '))
print(f'Nome é igual a {nome}')
print(f'Media é igual a {media}')
if media < 7:
   print(f'Situação da pessoa {nome} é igual a Reprovado')
else:
    print(f'Situação da pessoa {nome} é igual a Aprovado')'''

aluno = {}
aluno ['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média de {aluno["nome"]}:'))
if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f'   --  {k} é igual a {v}')