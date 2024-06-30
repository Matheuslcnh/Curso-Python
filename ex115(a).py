from uteis.curso.lib import *
from time import sleep
from uteis.curso.arquivo import *

arq = 'curso.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastras nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        #cabeçalho('Opção 1')
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Opcão 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema...Até logo! ')
        break
    else:
        print('\033[31mErro! Digite uma opção valida\033[m')
    sleep(2)
    