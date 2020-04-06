from src.txt import *
from src.controle import *
from src.html import *

opcao = str(input('Informe quantos registros gostaria de carregar: ')).strip()
while not isint(opcao):
    print('Opção inválida!')
    opcao = str(input('Informe quantos registros gostaria de carregar: ')).strip()

lista = carregar_txt('usuarios', opcao)
relatorio(lista)

opcao = str(input('Gostaria de exportar o relatório para HTML? [S/N] ')).strip().upper()[0]
while opcao not in 'SN':
    print('\33[31mOpção inválida!\33[m')
    opcao = str(input('Gostaria de exportar o relatório para HTML? [S/N] ')).strip().upper()[0]

if opcao == 'S':
    escrever_html(lista)
