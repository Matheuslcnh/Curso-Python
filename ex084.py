temp = []
princ = []
mai = men = 0
while True:
    temp.append(input('Nome :'))
    temp.append(float(input('Peso :')))
    
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp =input('Quer continuar [S/N]:')
    if resp in 'Nn':
        break
print(f'Ao todo tem {len(princ)} pessoas.')
print(f'O maior peso foi de {mai} Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi de {men} kg. Peso de', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}', end='')
print()