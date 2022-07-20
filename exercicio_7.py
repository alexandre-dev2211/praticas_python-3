# Identificando operações matemáticas através de seu operador:

def operacoes():
    o = input('Digite o operador matemático de desejado: ')
    x = float(input('Digite o valor de "x": '))
    y = float(input('Digite o valor de "y": '))
    if o == "+":
        som = x + y
        print(f'O resultado da soma de (x + y) é: {som}')
    elif o == "-":
        sub = x - y
        print(f'O resultado subtração (x - y) é igual a: {sub}')
    elif o == "*":
        mult = x * y
        print(f'O resultado da multiplicação (x * y) é: {mult}')
    elif o == "/":
        div = x / y
        print(f'O resultado da divisão (x / y) é: {div}')    



operacoes()
