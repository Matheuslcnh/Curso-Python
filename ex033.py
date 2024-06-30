a = int(input('Digite o 1° numero:'))
b = int(input('Digite o 2° numero:'))
c = int(input('Digite o 3° numero:'))

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
    
    
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('o menor valor é {}'.format(menor))
print('o maior valor é {}'.format(maior))

