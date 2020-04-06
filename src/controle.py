from src.utilitario import *


def relatorio(dados):
    print(f'{"ACME Inc.":<10}{"Uso do espaço em disco pelos usuários":^60}')
    print('-' * 70)
    print(f'{"Nr.":<4}{"Usuário":<15}{"Espaço utilizado":<20}{"% de uso":<15}')
    print()
    for usuario in dados:
        print(f'{usuario["id"]:<4}'
              f'{usuario["nome"]:<15}'
              f'{funcoes["utilizado"](usuario["espaco"]):>10} MB'
              f'{funcoes["percent"](dados, usuario["espaco"]):>14}')
    print()
    print(f'Espaço total ocupado: {funcoes["total"](dados)} MB')
    print(f'Espaço médio ocupado: {funcoes["media"](dados)} MB')