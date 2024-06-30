'''while True:
    sexo = input('Digite o sexo: ').upper().strip()
    if sexo == 'F' or sexo == 'M':
        print('Correto')
        break
    else:
        print('Digite de novo')'''
        
        
sexo = input('Informe seu sexo: ').strip().upper()[0]
while sexo not in 'MnFf':
    sexo = input('Dados invalidos. Informe seu sexo: ').strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))   

