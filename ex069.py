tot18 = tot18 = totM20 = h = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F]:').strip().upper()[0]
    
    if idade >=18:
        tot18 +=1  
    if sexo == 'M':
        h +=1
    if sexo == 'F' and idade < 20:
        totM20 +=1
        
        
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar: [S/N]').strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {h} homens cadastrados')
print(f'Temos {totM20} mulheres com menos de 20 anos')
    
    
    
    
    
    
    
    
    