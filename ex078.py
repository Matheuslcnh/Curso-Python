lista = []
for cont in enumerate(lista):
    print()
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para posição {cont}: ')))

print(f'Você digitou os valores {lista}')
print(f'O maior valor foi {max(lista)} na posição ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end='')
print(f'O menor valor foi {min(lista)} na posição ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end='')
print()


