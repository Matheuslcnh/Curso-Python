matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]:'))
print('=-'*30)        
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]}]', end='')
        if matriz[linha][coluna] % 2 ==0:
            spar += matriz[linha][coluna]
    print()
print('=-'*30)
print(f'A soma dos valores pares é {spar}')
for linha in range(0, 3):
    scol += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for coluna in range(0, 3):
    if coluna == 0:
        mai = matriz[1][coluna]
    elif matriz[1][coluna]> mai:
        mai = matriz[1][coluna]
print(f'O maior elemento da segunda linha é {mai}')
