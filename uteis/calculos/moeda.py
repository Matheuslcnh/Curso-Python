'''def dobro(n):
    return n * 2

def metade(n):
    return n / 2

def aumentar(n):
    v = n * 10/100
    vf = (v + n)
    return vf

def diminuir(n):
    v = n * 13/100
    vf = (n - v)
    return vf

def moeda(n):
    if moeda(n) == True:
        return (f'R${n:.2f}').replace('.',',')
    elif moeda(n) == False:
        return (f'R${n:.2f}')'''
    
def aumentar(preço=0, taxa=0, format=False):
    res = preço + (preço * taxa/100)
    return res if format == False else moeda(res)


def diminuir(preço=0, taxa=0, format=False):
    res = preço - (preço * taxa/100)
    return res if format == False else moeda(res)

def dobro (preço=0, format=False):
    res = preço * 2 
    return res if format == False else moeda(res)

def metade(preço=0, format=False):
    res = preço / 2
    return res if format == False else moeda(res)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def resumo(preço=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' *30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'A metade do preço: \t{metade(preço, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'Com {taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' *30)