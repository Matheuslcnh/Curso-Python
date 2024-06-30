n = soma = cont = 0
while True:
    n = int(input('Digite um numero [999 para parar]: '))
    cont +=1
    if n == 999:
        break
    soma += n
print(f'Foram digitados {cont} numeros e a soma entre eles foi {soma}')