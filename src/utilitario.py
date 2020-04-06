funcoes = {
    'utilizado': lambda espaco: f'{(espaco / 1024) / 1024:.2f} MB',
    'percent': lambda lista, espaco: f'{((espaco * 100) / (sum([usuario["espaco"] for usuario in lista]))):.2f}%',
    'total': lambda lista: f'{(sum([usuario["espaco"] for usuario in lista]) / 1024) / 1024:.2f} MB',
    'media': lambda lista: f'{((sum([usuario["espaco"] for usuario in lista]) / 1024) / 1024) / len(lista):.2f} MB'
}