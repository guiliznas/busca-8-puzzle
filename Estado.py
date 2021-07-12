class Estado:
    def __init__(self, matriz, parent=None):
        # [[],[],[]]
        self.matriz = matriz
        #self.parent
        #self.caminho
        self.heuristica = self.calcularHeuristica()
        self.custo = 0 if parent is None else parent.custo + 1
        self.estimativa = self.custo + self.heuristica
        return

    def calcularHeuristica(self):

        return self._heuristicaSimples()

    def _heuristicaSimples(self):
        # quantidade de posicoes erradas

        lista = [item for sublist in self.matriz for item in sublist]

        ordenado = lista[:]
        ordenado.sort()

        count = 0
        for ind, val in enumerate(lista):
            if ordenado[ind] != val:
                count += 1

        return count

    def _heuristicaAvancada(self):
        # distancia de manhattan (diferenca de X + diferenca de Y)
        return 0
    
    def filhos(self, tamanho=3):

        valor_vazio = 0
        filhos = []

        vazio = [(index, row.index(valor_vazio)) for index, row in enumerate(self.matriz) if valor_vazio in row]

        vazio = vazio[0]

        # para cima
        if vazio[0] - 1 > -1:
            matriz_cima = [itens[:] for itens in self.matriz]
            matriz_cima[vazio[0]][vazio[1]] = self.matriz[vazio[0] -1][vazio[1]]
            matriz_cima[vazio[0]-1][vazio[1]] = 0
            estado_cima = Estado(matriz=matriz_cima, parent=self)
            filhos.append(estado_cima)
        # para direita
        if vazio[1] + 1 < tamanho:
            matriz_cima = [itens[:] for itens in self.matriz]
            matriz_cima[vazio[0]][vazio[1]] = self.matriz[vazio[0]][vazio[1] + 1]
            matriz_cima[vazio[0]][vazio[1] + 1] = 0
            estado_cima = Estado(matriz=matriz_cima, parent=self)
            filhos.append(estado_cima)
        # para baixo
        if vazio[0] + 1 < tamanho:
            matriz_cima = [itens[:] for itens in self.matriz]
            matriz_cima[vazio[0]][vazio[1]] = self.matriz[vazio[0] + 1][vazio[1]]
            matriz_cima[vazio[0]+1][vazio[1]] = 0
            estado_cima = Estado(matriz=matriz_cima, parent=self)
            filhos.append(estado_cima)
        # para esquerda
        if vazio[1] - 1 > -1:
            matriz_cima = [itens[:] for itens in self.matriz]
            matriz_cima[vazio[0]][vazio[1]] = self.matriz[vazio[0]][vazio[1] - 1]
            matriz_cima[vazio[0]][vazio[1] - 1] = 0
            estado_cima = Estado(matriz=matriz_cima, parent=self)
            filhos.append(estado_cima)

        return filhos

    def ehObjetivo(self):
        ## Verificar outros tipos de objetivos
        lista = [item for sublist in self.matriz for item in sublist]

        ordenado = lista[:]
        ordenado.sort()

        return lista == ordenado

    def comparar(self, nodo):

        lista = [item for sublist in self.matriz for item in sublist]
        lista_nodo = [item for sublist in nodo.matriz for item in sublist]

        return lista == lista_nodo
    
    def __str__(self):
        return '\n'.join([', '.join([str(val) for val in itens]) for itens in self.matriz]) + '\n' + "Custo: {}\nHeuristica: {}\n".format(self.custo, self.heuristica)