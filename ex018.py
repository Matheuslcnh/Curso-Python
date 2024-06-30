import math

angulo = int(input('Digite um Ângulo: '))
sen = math.sin(math.radians(angulo))
print(f'O angulo {angulo} tem o SENO de {sen :.2f}')
cos = math.cos(math.radians(angulo))
print(f'O angulo {angulo} tem o COSSENO de {cos :.2f}')
tan = math.tan(math.radians(angulo))
print(f'O angulo {angulo} tem a TANGENTE de {tan :.2f}')


