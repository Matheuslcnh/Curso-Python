from datetime import date
n = int(input('Digite o ano :'))
if n == 0:
    n = date.today().year
if (n % 4) == 4 and n % 100 != 0 or n % 400 == 0:
    print('o Ano {} é BISSEXTO'.format(n))
else:
    print('o Ano {} não é BISSEXTO'.format(n))
    
    