from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
atual = date.today().year
categoria = atual - ano
print(f'{categoria} anos')
if categoria <= 9:
    print('Mirim')
elif categoria <= 14:
    print('Infantil')
elif categoria <= 19:
    print('Junior')
elif categoria <= 25:
    print('Senior')
elif categoria > 20:
    print('Master')
    
