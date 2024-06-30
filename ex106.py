from time import sleep

c = ('\033[m',    # 0 - sem cores
    '\033[0;33;41m', #1 - vermelho
    '\033[0;30;42m', #2 - verde
    '\033[0;33;43m', #3 - amarelo
    '\033[0;33;44m', #4 - azul
    '\033[0;30m', #5 - branco
    );

def ajuda(com):
    titulo(f'ACESSANDO O MANUAL DO COMANDO \'{com}\'', 4)
    print(c[5], end='')
    help(com)
    print(c[0], end='')
    sleep(2)
    

def titulo(msg, cor=0):
    tam = len(msg) +4
    print(c[cor], end='')
    print('~' *tam)
    print(f' {msg}')
    print('~'*tam)
    print(c[0], end='')
    sleep(1)

comando = ''
while True:
    titulo('SISTEMA AJUDA PyHELP', 2)
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda (comando)
titulo('ATÉ LOGO', 1)