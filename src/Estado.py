from utils import Utils, MODO_CUSTO_UNIFORME, MODO_A_SIMPLES, MODO_A_MELHORADO, MODO_A_INVERSOES

class Estado:

    def __init__(self, matriz, parent=None):
        # Matriz para representar o tabuleiro
        self.matriz = matriz
        # O pai do nodo atual
        self.parent = parent
        # Calcular o custo do nodo atual
        self.custo = 0 if parent is None else parent.custo + 1
        # Calcular a heuristica para o tabuleiro atual
        self.heuristica = self.calcularHeuristica()
        # Calcular a estimativa para o nodo atual
        self.estimativa = self.custo + self.heuristica
        return

    def calcularHeuristica(self):
        """
            Calcular a heuristica do nodo atual conforme configuracoes da busca
        """

        MAP_HEURISTICAS = {
            MODO_CUSTO_UNIFORME: self._custoUniforme,
            MODO_A_SIMPLES: self._heuristicaSimples,
            MODO_A_MELHORADO: self._heuristicaAvancada,
            MODO_A_INVERSOES: self._heuristicaInversoes
        }

        return MAP_HEURISTICAS[Utils.modo]()

    def _custoUniforme(self):
        return self.custo

    def _heuristicaSimples(self):
        """
            Logica simples, considerando somente a quantidade de posicoes erradas.
        """

        # Transforma a matriz em uma lista
        lista = [item for sublist in self.matriz for item in sublist]

        ordenado = Utils.objetivo

        # Contar quantos fora de posicao ha
        count = 0
        for ind, val in enumerate(lista):
            if ordenado[ind] != val:
                count += 1

        return count

    def _heuristicaInversoes(self):
        """
            Logica mediana, considerando a quantidade de inversoes necessarias.
        """

        lista = [item for sublist in self.matriz for item in sublist]

        numInversoes = 0
        for i in range(len(lista)):
            for j in range(i+1, len(lista)):
                if lista[i] > 0 and lista[j]>lista[i]:
                    numInversoes += 1

        return numInversoes

    def _heuristicaAvancada(self):
        """
            Logica um pouco mais avancada, utilizando a Distancia de Manhattan para definir a heuristica
        """

        # Calcular Distancia de manhattan
        distancia = 0
        for linha in self.matriz:
            for item in linha:
                if item > 0:
                    posicao_atual = self._buscaValor(item)
                    posicao_certa = Utils.dic_map_valores[item]
                    distancia += abs(posicao_certa[0]-posicao_atual[0]) + abs(posicao_certa[1]-posicao_atual[1])

        return distancia
    
    def _buscaValor(self, valor, matriz=None):
        """
            Encontrar posicao na matriz de algum valor numerico
        """

        if matriz is None:
            matriz = self.matriz

        # Busca o valor na matriz e retorna uma lista de tuplas
        vazio = [(index, row.index(valor)) for index, row in enumerate(matriz) if valor in row]

        # Se tiver encontrado alguma ocorrencia, seleciona a primeira
        if len(vazio) == 0:
            return None
        vazio = vazio[0]

        return vazio

    def filhos(self):
        """
            Busca dos filhos de cada nodo.
            Considerando que soh eh possivel ter 4 filhos no maximo, uma para cada direcao.
        """

        tamanho = Utils.tamanho

        valor_vazio = 0
        filhos = []

        # Encontra a posicao do valor vazio
        vazio = self._buscaValor(valor_vazio, matriz=self.matriz)

        # Tentar movimentar para cima
        if vazio[0] - 1 > -1:
            matriz_cima = [itens[:] for itens in self.matriz]
            matriz_cima[vazio[0]][vazio[1]] = self.matriz[vazio[0] -1][vazio[1]]
            matriz_cima[vazio[0]-1][vazio[1]] = 0
            estado_cima = Estado(matriz=matriz_cima, parent=self)
            filhos.append(estado_cima)
            
        # Tentar movimentar para a direita
        if vazio[1] + 1 < tamanho:
            matriz_direita = [itens[:] for itens in self.matriz]
            matriz_direita[vazio[0]][vazio[1]] = self.matriz[vazio[0]][vazio[1] + 1]
            matriz_direita[vazio[0]][vazio[1] + 1] = 0
            estado_direita = Estado(matriz=matriz_direita, parent=self)
            filhos.append(estado_direita)

        # Tentar movimentar para baixo
        if vazio[0] + 1 < tamanho:
            matriz_baixo = [itens[:] for itens in self.matriz]
            matriz_baixo[vazio[0]][vazio[1]] = self.matriz[vazio[0] + 1][vazio[1]]
            matriz_baixo[vazio[0]+1][vazio[1]] = 0
            estado_baixo = Estado(matriz=matriz_baixo, parent=self)
            filhos.append(estado_baixo)

        # Tentar movimentar para esquerda
        if vazio[1] - 1 > -1:
            matriz_esquerda = [itens[:] for itens in self.matriz]
            matriz_esquerda[vazio[0]][vazio[1]] = self.matriz[vazio[0]][vazio[1] - 1]
            matriz_esquerda[vazio[0]][vazio[1] - 1] = 0
            estado_esquerda = Estado(matriz=matriz_esquerda, parent=self)
            filhos.append(estado_esquerda)

        return filhos

    def ehObjetivo(self):
        """
            Verificar se o nodo atual eh o objetivo final.
        """
        return self.matriz == Utils.objetivo_matriz

    def comparar(self, nodo):
        """
            Comparacao entre dois nodos.
        """
        return nodo.matriz == self.matriz
    
    def apresentarCaminho(self):
        """
            Apresentar o caminho para chegar ate o nodo atual
        """

        # Lista auxiliar para o caminho
        lista = []

        # Iniciando busca no nodo atual
        nodo = self

        # Enquanto o nodo tiver um pai, vai adicionando ele na lista
        # e selecionando o pai para verificar
        while nodo.parent is not None:
            lista.insert(0, nodo)
            nodo = nodo.parent
        
        # Inserir o nodo inicial da arvore, que nao possui pai
        lista.insert(0, nodo)

        print("**"*20)
        print("Caminho para solucionar:")
        for nodo in lista:
            print(nodo)
        print("**"*20)
        return len(lista) - 1

    def __str__(self):
        return '\n'.join([' '.join([str(val) if val != 0 else '_' for val in itens]) for itens in self.matriz]) + '\n' + "Custo: {}\nHeuristica: {}\n".format(self.custo, self.heuristica)