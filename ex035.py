print('---' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('-==' * 30)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Da para formar um triangulo ')
else:
    print('nao da para formar um triangulo')
    
if r1 == r2 == r3:
    print('Esse triangulo é equilatero')
elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
    print('Triagulo isosceles')
elif r1 != r2 != r3:
    print('Triangulo escaleno')

