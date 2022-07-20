# Calculando o volume de um cilindro:

def volume():
    r = float(input('Digite o raio do cilindro: '))
    a = float(input('Digite a altura do cilindro: '))
    v = 3.14 * r ** 2 * a
    print(f'O volume do cilindro é igual á: {v}')


volume()
    