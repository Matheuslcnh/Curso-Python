opcao = 'S'
soma = quant = media = maior = menor = 0
while opcao in 'S':
    n = int(input('Digite um numero: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opcao = input('Quer continuar? [S/N]').upper()[0]
media = soma / quant
print('vc digitou {} numeros e a media foi {}'.format(quant, media))
print('o maior valor foi {} e o menor foi {}'.format(maior, menor))