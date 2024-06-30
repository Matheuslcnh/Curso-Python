'''primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 -1) *razao
for c in range(primeiro, decimo + razao, razao):
    print(c)'''
    


primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}  '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')