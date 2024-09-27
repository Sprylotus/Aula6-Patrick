import os

os.system('cls')


list_previsoes = ['Ensolarado', 'Nublado', 'Chuvoso', 'Tempestade', 'Ensolarado']

for c in list_previsoes:
    if c == 'Ensolarado':
        print(f'{c}: Aproveite e passeie!')
    else:
        print(f'{c}: Não esqueça o guarda-chuva!')