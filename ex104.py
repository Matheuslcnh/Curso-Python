def leiaInt(msg):
    ok = False
    valor =0 
    while True:
        n = (input(msg))
        if n.isnumeric():
            valor= int(n)
            ok = True
        else:
            print('\033[0;31mERRO! digite um numero inteiro\033[m')
        if ok:
            break
    return valor
        

num = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {num}')