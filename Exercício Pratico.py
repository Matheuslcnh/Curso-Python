from time import sleep

def listar_filmes():
    if conteudo:
        print('Filmes adicionados:')
        for i in range(0, len(conteudo), 2):
            print(f'{(i // 2) + 1}. Filme: {conteudo[i]}, Gênero: {conteudo[i + 1]}')
            '''Quando i é 0, 0 // 2 é 0.
            Quando i é 2, 2 // 2 é 1.
            Quando i é 4, 4 // 2 é 2.'''
    else:
        print('Nenhum filme adicionado ainda.')

conteudo = []

while True:
    print('-='*15)
    print('Escolha a Opção:\n1. Adicionar filme\n2. Listar Filmes\n3. Parar')
    print('-='*15)
    opcao = int(input('\033[0;32mDigite um número da opção: \033[m'))
    if opcao == 1:
        sleep(1.5)
        print('\033[0;32mCerto! Você quer adicionar um Filme. \033[m')
        sleep(2)
        print('.')
        sleep(1)
        print('.')
        f = input('\033[0;31mDigite o nome do Filme: \033[m')
        sleep(1.5)
        g = input(f'\033[0;36mDigite o nome do Gênero do filme {f}: \033[m')
        sleep(1)
        conteudo.append(f)
        conteudo.append(g)
        s_n = input('Quer continuar? R:  ').strip().upper()[0]
        if s_n == 'N':
            print('\033[0;32mMuito obrigado por usar o nosso código!  \033[m')
            sleep(2)
            sleep(1)
            print('Finalizando....')
            sleep(2)
            break
    elif opcao == 2:
        print('\033[0;32mOk! Vamos listar todos os filmes \033[m')
        sleep(2)
        listar_filmes()
    elif opcao == 3:
        print('\033[0;32mMuito obrigado por usar o nosso código!  \033[m')
        sleep(2)
        print('Saindo...')
        sleep(2)
        break
    else:
        print('\033[0;31mOpção inválida. Tente novamente.\033[m')
        
print('-='*15)
print('Filmes e Gêneros adicionados:')
print('-='*15)

if conteudo:
    for i in range(0, len(conteudo), 2):
        print(f'\033[0;36m{(i // 2) + 1}\033[m. Filme: {conteudo[i]}, Gênero: {conteudo[i + 1]}')
else:
    print('\033[0;31mNenhum filme adicionado.\033[m')





        
    