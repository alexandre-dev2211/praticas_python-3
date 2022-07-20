# Calculando o rendimento de um veículo com base nas variáveis distância percorrida e consumo de combustível:

def rendimento():
    km = float(input('Digite a distância percorrida (Km): '))
    l = float(input('Digite a quantidade de combustível consumida (l): '))
    r = km / l
    if r < 8:
        print(f'Vender Veículo! Rendimento de {r} Km/l')
    elif r in range(8, 14):
        print(f'Veículo Econômico! Rendimento de {r} Km/l')
    elif r > 12:
        print(f'Veículo Muito Econômico! Rendimento de {r} Km/l')


rendimento()
