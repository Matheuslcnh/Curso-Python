n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um outro valor: '))
print('''[1]somar
[2]multiplicar
[3]maior
[4]novos numeros
[5]sair do programa''')
menu = int(input('Digite o numero: '))

while menu <=4:
    
    if menu == 1:
        soma = n1 + n2
        print('A soma é:'.format(soma))
        break
    if menu == 2:
        mult = n1 * n2
        print('A multiplicação dos numeros {} e {} é {}'.format(n1, n2, mult))
        break
    if menu == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
        break
    if menu == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite um outro valor: '))
        print('''[1]somar
[2]multiplicar
[3]maior
[4]novos numeros
[5]sair do programa''')
        menu = int(input('Digite o numero: '))

if menu == 5:
    print('Programa encerrado')

        