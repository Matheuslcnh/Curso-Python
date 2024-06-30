n = int(input('numero: '))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(n, ' não é primo')
            break
    else:
        print(n, ' é primo')
            