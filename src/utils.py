MODO_CUSTO_UNIFORME = 'custo_uniforme'
MODO_A_SIMPLES = 'a_simples'
MODO_A_MELHORADO = 'a_complexo'
MODO_A_INVERSOES = 'a_inversoes'

class Utils:
    tamanho = 3
    modo = MODO_CUSTO_UNIFORME
    objetivo = []
    objetivo_matriz = []
    dic_map_valores = {}

    def preencher_map_coordenadas_objetivo(matriz=None):
        if matriz is None:
            matriz = Utils.objetivo_matriz

        for valor in Utils.objetivo:
            Utils.dic_map_valores[valor] = [(index, row.index(valor)) for index, row in enumerate(matriz) if valor in row][0]

    def lista_para_matriz(lista, tamanho=None):
        if tamanho is None:
            tamanho = Utils.tamanho

        matriz = []
        lista_aux = lista[:]

        while(len(lista_aux) > 0):
            matriz.append(lista_aux[:tamanho])
            lista_aux = lista_aux[tamanho:]

        return matriz