import random
from time import sleep
contador = 0
cores = ["vermelho", "verde", "azul", "amarelo", "roxo"]

print("\033[0;32mDada as cores: \033[m", (cores))
nome = input('QUAL É O SEU NOME? R: ').upper()
sleep(0.7)
print(f'Olá {nome}! Seja Bem vindo ao Nosso Exercício 2!')
print('-='*15)
print('\n\033[0;36mVocê terá 3 chances para Acertar, Caso contrário, o programa será Encerrado!\033[m')
sleep(1.5)
print('BOA SORTE!!')
sleep(2)

while True:
    print('-='*15)
    print('       JOGO ADIVINHAÇÃO')
    print('-='*15)
    
    cor_aleatoria = random.choice(cores)
    usuario = (input("\033[0;33mEscolha uma cor: \033[m"))
    if usuario == cor_aleatoria:
        print(f'\033[0;36mParabéns {nome}!!!\033[m')
        sleep(2)
        print('\033[0;36mVocê acertou a cor!!\033[m')
        break
    elif usuario != cor_aleatoria:
        contador +=1
        print('\033[0;33mVocê não acertou a cor.\033[m') 
        if contador == 3:
            print('\033[0;31mPutss!! Você não conseguiu acertar...\033[m')
            sleep(1)
            print("\033[0;31mCódigo encerrado!!\033[m")
            break   

    
