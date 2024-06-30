import random
print('-='*20)
while True:
    usuario = int(input('Diga um valor: '))
    
    comp = random.randint(0, 10)
    soma = usuario + comp
    cont = 0
    tipo = ' '
    while tipo not in 'PpIi':
        tipo= input('Par ou Impar:').strip().upper()[0]
    print(f'Você jogou {usuario} e o computador {comp}. Total deu {soma}', end=' ')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if soma % 2 ==0:
            print('Voce venceu')
            cont += 1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if soma % 2 ==1:
            print('Voce venceu')
            cont += 1
        else:
            print('Voce perdeu')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {cont} vezes')
        
        

    




