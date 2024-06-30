from time import sleep
produto = float(input('Digite o valor a ser pago: '))

print('Voce tem tres opcões de pagamento....')
sleep(1)
print('Digite 1 para dinheiro/cheque, com desconto de 10%')
print('Digite 2 para Cartão, com 5% de desconto')
print('Digite 3 para parcelar em ate 2x no cartao')
print('Digite 4 para 3x ou mais no cartão, porem com juros de 20% ')
escolha = int(input('Digite a forma: '))

if escolha == 1 :
    print('O valor a ser pago no dinheiro/cheque será de R${:.2f}'.format(produto - (produto * 10/100)))
elif escolha == 2:
    print('o valor a ser pago no cartao será de R${:.2f} '.format(produto - (produto * 5/100)))
elif escolha == 3 :
    print('o valor a ser pago em 2x no cartao será de R${:.2f} mensais. O valor total ficou em R${}'.format(produto / 2, produto))
elif escolha == 4 :
    total = produto + (produto * 20/100)
    total_parcela = int(input('Quantas parcelas: '))
    parcela = total / total_parcela
    print('o valor a ser pago em {}x no cartao será de R${:.2f} com juros'.format(total_parcela, parcela))
    print('A compra de R${:.2f} vai custar R${:.2f} no final'.format(produto, total))