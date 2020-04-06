from src.txt import *
from src.controle import *
from src.html import *

lista = carregar_txt('usuarios')
relatorio(lista)

opcao = str(input('Gostaria de exportar o relatório para HTML? [S/N] ')).strip().upper()[0]
while opcao not in 'SN':
    print('\33[31mOpção inválida!\33[m')
    opcao = str(input('Gostaria de exportar o relatório para HTML? [S/N] ')).strip().upper()[0]

if opcao == 'S':
    escrever_html(lista)
