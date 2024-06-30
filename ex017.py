import math
oposto = int(input('Digite o cateto oposto: '))
adjacente = int(input('Digite o cateto adjacente: '))
hip = math.hypot(oposto, adjacente)

print('A hipotenusa será: {}'.format(hip))



#ou



oposto = int(input('Digite o cateto oposto: '))
adjacente = int(input('Digite o cateto adjacente: '))
hip = (oposto **2 + adjacente **2) ** (1/2)

print('A hipotenusa será: {:.1f}'.format(hip))