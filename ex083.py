ex = input('Digite a expressão: ')
pilha = []
for simb in ex:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta valida')
else:
    print('Sua expresssão esta invalida')