num = list()
while True:
    num.append(int(input('Digite um numero: ')))
    resp = input('Quer continuar [S/N]:').strip().upper()[0]
    if resp in 'Nn':
        break
pares = list()
impares = list()
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
