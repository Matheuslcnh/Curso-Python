from datetime import datetime
dados = {}
dados['nome'] = input('Nome: ')
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 nao tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = ((dados['contratação'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f' --{k} tem o valor {v}')