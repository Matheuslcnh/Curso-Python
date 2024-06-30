from datetime import date
atual = date.today().year
contador_maior = 0
contador_menor = 0
for i in range(7):
    ano = int(input('Digite seu ano de nascimento: '))
    atual = date.today().year
    dif = atual - ano
    
    if dif >= 21:
        contador_maior += 1
    else:
        contador_menor += 1

print('Maiores de 18, são {} pessoas'.format(contador_maior))
print('Menores de 18, são {} pessoas'.format(contador_menor))
    