pessoa = {}
galera = []
soma = media =0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: [M/F]: ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('Erro! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = input('Quer continuar? [S/N]: ').upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N')
    if resp == 'N':
        break
print('-='*30)
print(f'A) Ao todo tempos {len(galera)} pessoas cadastradas')
media =soma / len(galera)
print(f'B) A media de idade é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<<ENCERRADO>>>')

