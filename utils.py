class Utils:
    tamanho = 3

    def lista_para_matriz(lista, tamanho=None):
        if tamanho is None:
            tamanho = Utils.tamanho

        matriz = []
        lista_aux = lista[:]

        while(len(lista_aux) > 0):
            matriz.append(lista_aux[:tamanho])
            lista_aux = lista_aux[tamanho:]

        return matriz