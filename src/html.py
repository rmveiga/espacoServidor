from src.utilitario import *


def codigo_html(dados: list):
    numero = usuario = espaco = percent = ''
    total = media = html = ''
    for pessoa in dados:
        numero = numero + f'<p>{pessoa["id"]}</p>'
        usuario = usuario + f'<p>{pessoa["nome"]}</p>'
        espaco = espaco + f'<p id="espaco">{funcoes["utilizado"](pessoa["espaco"])}</p>'
        percent = percent + f'<p id="percent">{funcoes["percent"](dados, pessoa["espaco"])}</p>'

    total = f'{funcoes["total"](dados)}</p>'
    media = f'{funcoes["media"](dados)}</p>'
    html = '''
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="utf-8">
        <style>
            #coluna1{
                float: left;
                width: 100px;
            }
            #coluna2{
                float: left;
                width: 200px;
            }
            #coluna3{
                float: left;
                width: 200px;
            }
            #coluna4{
                float: left;
                width: 200px;
            }
            #espaco{
                text-align: right;
                width: 100px;
            }
            #percent{
                text-align: right;
                width: 50px;                
            }
            #rodape{
                clear: both;
            }
        </style>
    </head>
    <body>
    <div id="geral">
        <div id="cabecalho">
            <h1>ACME Inc.</h1>
            <h2>Uso do espaço em disco pelos usuários</h2>
            <hr>
        </div>
        <div id="colunas">
            <div id="coluna1">
                <p class="cabecalho">Nro.</p>''' + numero + '''
            </div>
            <div id="coluna2">
                <p class="cabecalho">Usuário</p>''' + usuario + '''
            </div>
            <div id="coluna3">
                <p class="cabecalho">Espaço utilizado</p>''' + espaco + '''
            </div>
            <div id="coluna4">
                <p class="cabecalho">% de uso</p>''' + percent + '''
                <br>
            </div>
        </div>
        <div id="rodape">
            <p>Espaço total ocupado: ''' + total + '''
            <p>Espaço médio ocupado: ''' + media + '''
        </div>
    </div>
    </body>
</html>'''

    return html


def escrever_html(dados: list):
    html = open('consumo.html', 'w', encoding='utf-8')
    html.write(codigo_html(dados))
    html.close()
    print('Arquivo HTML exportado com sucesso!')


if __name__ == '__main__':
    print('teste {}'.format('1'))
