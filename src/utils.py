MODO_CUSTO_UNIFORME = 'custo_uniforme'
MODO_A_SIMPLES = 'a_simples'
MODO_A_MELHORADO = 'a_complexo'

class Utils:
    tamanho = 3
    modo = MODO_CUSTO_UNIFORME

    def lista_para_matriz(lista, tamanho=None):
        if tamanho is None:
            tamanho = Utils.tamanho

        matriz = []
        lista_aux = lista[:]

        while(len(lista_aux) > 0):
            matriz.append(lista_aux[:tamanho])
            lista_aux = lista_aux[tamanho:]

        return matriz