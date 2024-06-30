from uteis.curso.lib import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('houve erro')
    else:
        print(f'Criado {nome}')
        
def lerArquivo(nome):
    try:
        a= open(nome, 'rt')
    except:
        print('erro ao ler')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.readlines())

