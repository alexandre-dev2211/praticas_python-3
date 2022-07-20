# Comparando dois números inteiros e retornando o maior deles:

def maior():
    x1 = int(input('Digite o valor para "x1": '))
    x2 = int(input('Digite o valor para "x2": '))
    if x1 > x2:
        print('x1 é o maior número.')
    elif x2 > x1:
        print('x2 é o maior número.')
    elif x1 == x2:
        print('x1 e x2 são iguais.')    



maior()