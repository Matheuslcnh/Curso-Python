def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('Erro. Digite um numero inteiro valido')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('Erro! Digite um numero real valido')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida')
            return 0 
        else:
            return n


n1 = leiaInt('Digite um valor: ')
n2 = leiaFloat('Digite um real: ')
print(f'O valor digitado foi {n1} e {n2}')


