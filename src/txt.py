def carregar_txt(arquivo):
    try:
        usuario = dict()
        lista = list()
        cont = 1

        txt = open(arquivo + '.txt', 'r')
        for pessoa in txt.readlines():
            usuario['id'] = cont
            usuario['nome'] = pessoa.split()[0]
            usuario['espaco'] = int(pessoa.split()[1])
            lista.append(usuario.copy())
            usuario.clear()
            cont += 1

        txt.close()
        return lista
    except Exception as erro:
        print(f'Falha ao carregar o arquivo: {erro}')
