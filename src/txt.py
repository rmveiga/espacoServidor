def carregar_txt(arquivo, registros):
    try:
        usuario = dict()
        lista = list()
        cont = 1

        txt = open(arquivo + '.txt', 'r')
        for pessoa in txt.readlines():
            usuario['id'] = 1
            usuario['nome'] = pessoa.split()[0]
            usuario['espaco'] = int(pessoa.split()[1])
            lista.append(usuario.copy())
            usuario.clear()

            if cont == int(registros):
                break
            else:
                cont += 1

        cont = 1
        lista.sort(key=lambda i: i['espaco'], reverse=True)
        for pessoa in lista:
            pessoa['id'] = cont
            cont += 1

        txt.close()
        return lista
    except Exception as erro:
        print(f'Falha ao carregar o arquivo: {erro}')
