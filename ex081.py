lista = []
while True:
    valor = lista.append(int(input('Digite um valor: ')))
    op = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if op in 'Nn':
       break
    elif op in 'Ss':
        print('Valor adicionado')
print('-='*30)
print(f'Voce digitou {len(lista)} elementos')
lista.sort()
print(f'Os valores em ordem crescente são {lista}')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 nao esta ana lista')
print('-='*30)

       
    