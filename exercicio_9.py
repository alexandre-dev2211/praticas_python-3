# Definindo um triângulo com base em suas medidas:

b = float(input('Digite o valor da base para o triângulo: '))

l1 = float(input('Digite o valor do lado para o triângulo: '))

l2 = float(input('Digite o valor do outro lado para o triângulo: '))

def triangulo():
    if b < (l1 + l2) and l1 < (b + l2) and l2 < (b + l1):
        print('É um Triângulo')
    else:
        print('Não é um Triângulo')


triangulo()

def tipo():
    if b == l1 == l2:
        print('Triângulo Equilátero!')
    elif b == l1 or b == l2 or l1 == l2:
        print('Triângulo Isóceles!')
    elif b != l1 != l2:
        print('Triângulo Escaleno!')


tipo()
