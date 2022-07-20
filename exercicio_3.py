# Função que converte temperatura de Celsius para Farenheit:

def conversao():
    c = float(input('Digite a temperatura em graus Celsius: '))
    f = c * (9.0 / 5.0) + 32.0
    print(f'A temperatura é igual á: {f} Farenheit.')


conversao()