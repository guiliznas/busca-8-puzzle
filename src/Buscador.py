from Estado import Estado
from utils import Utils
import random

class Buscador:
    def __init__(self, tamanho=3, estadoInicial=None, modo=None, objetivo=None):

        # Salvar o tamanho do tabuleiro (numero de colunas)
        Utils.tamanho = tamanho
        self.tamanho = tamanho

        # Salvar o metodo de busca
        if modo:
            Utils.modo = modo
        else:
            modo = Utils.modo
        self.modo = modo
        print("Modo utilizado: {}".format(self.modo))

        self.objetivo_informado = objetivo

        if objetivo is not None:
            if isinstance(objetivo, str):
                objetivo = [int(val) for val in objetivo.split(',')]
            if len(objetivo) != tamanho*tamanho:
                print("Objetivo nao tem o tamanho adequado")
                objetivo = None
        if objetivo is None:
            objetivo = list(range(1, tamanho*tamanho))
            objetivo.append(0)
        Utils.objetivo = objetivo
        Utils.objetivo_matriz = Utils.lista_para_matriz(objetivo)
        Utils.preencher_map_coordenadas_objetivo()

        # Se nao foi informado um estado inicial, ele eh gerado
        if estadoInicial is None:
            print("Gerando estado inicial")
            # Gerar uma lista de numeros
            estadoInicial = list(range(tamanho*tamanho))
            # Embaralhar a lista de numeros
            random.shuffle(estadoInicial)

        # Formatando a lista para uma matriz
        matriz = Utils.lista_para_matriz(estadoInicial)

        # Verificando se a matriz eh valida, se nao for gera-se outra
        matriz = self.gerarMatrizValida(matriz)

        # Criando o estado pai
        nodo = Estado(matriz=matriz)
        print("Estado inicial: \n{}".format(nodo))

        # Iniciando as variaveis auxiliares
        self.visitados = []
        self.abertos = [nodo]
        self.expandidos = 0
        self.criados = 0
        self.max_abertos = 0

        return

    def gerarMatrizValida(self, matriz):
        """
            Gerar matrizes ate retornar uma valida
        """

        if not self.matrizValida(matriz):
            print("Matriz inválida")

        while self.matrizValida(matriz) is False:
            tamanho = self.tamanho
            lista = list(range(tamanho*tamanho))
            random.shuffle(lista)
            matriz = Utils.lista_para_matriz(lista)

        print("Matriz válida: {}".format(matriz))

        return matriz

    def matrizValida(self, matriz):
        """
            Utilizando a formula de Paridade de Permutacao para descobrir se o tabuleiro eh possivel de resolver
        """

        if self.objetivo_informado:
            return True

        # Retornando a matriz para uma lista
        lista = [item for sublist in matriz for item in sublist]

        count = 0
        # Para cada valor, contar quantos valores que estao depois dele deveriam estar antes.
        for i in range(len(lista)):
            for j in range(i+1, len(lista)):
                if lista[i] > 0 and lista[j]>lista[i]:
                    count += 1

        return (count % 2 == 0)

    def iniciarBusca(self):
        """
            Metodo principal para rodar a busca
        """

        # Se nao for uma matriz valida, parar execucao
        if not self.matrizValida(self.abertos[0].matriz):
            print("Impossível solucionar")
            return

        # Loop geral da busca
        while True:
            # Se nao tem mais nodos abertos, algo deu errado
            if len(self.abertos) == 0:
                return None

            # Pega o primeiro nodo da lista de abertos
            nodo = self.abertos.pop(0)
            self.criados += 1

            # Ja adiciona nos nodos visitados
            self.visitados.append(nodo)

            # Verificar se eh um objetivo
            ehObjetivo = nodo.ehObjetivo()

            # Se for objetivo, retorna o nodo
            if ehObjetivo:
                print("Encontrou resposta")
                return nodo

            # Se nao for objetivo
            # Pega os filhos do nodo em analise
            filhos = nodo.filhos()

            # Se tiver filhos
            if len(filhos) > 0:
                # Inserir os filhos na lista de nodos abertos
                self._inserirNodoAberto(estados=filhos)

    def _inserirNodoAberto(self, estados=[]):
        """
            Inserir na lista ordenada de nodos abertos
        """

        # Adicionar contagem nos nodos expandidos
        self.expandidos += len(estados)

        # Para cada estado recebido
        for estado in estados:
            # Verificar se o estado ja foi visitado
            if self.estaVisitado(estado):
                pass
            else:
                # Verificar se o estado ja esta aberto
                if self.estaAberto(estado):
                    self.reporEstadoAberto(estado)
                    pass
                else:
                    # Para cada estado novo, verifica qual a posicao dele na lista
                    pos = self.__pegarPosicao(estado=estado)
                    # Inserir o nodo na lista de abertos
                    self.abertos.insert(pos, estado)

        self.max_abertos = max(self.max_abertos, len(self.abertos))

        return

    def reporEstadoAberto(self, estado):
        """
            Caso o nodo exista um nodo aberto com o mesmo tabuleiro mas custo maior,
            troca pelo estado recebido.
        """

        posicao = -1

        for ind, aberto in enumerate(self.abertos):
            if estado.comparar(aberto) and estado.custo < aberto.custo:
                posicao = ind
                break

        if posicao > -1:
            self.abertos[posicao] = estado

        return

    def __pegarPosicao(self, estado=None):
        """
            Buscar a posicao do nodo na lista de nodos abertos conforme estimativa (custo + heuristica)
        """

        # Para cada nodo na lista de abertos
        for ind, nodo in enumerate(self.abertos):
            # Verifica se a estimativa do nodo eh maior que do estado sendo adicionado
            if nodo.estimativa > estado.estimativa:
                # Retornar a posicao que estava sendo verificada
                return ind

        # Caso nao foi encontrado uma posicao para inserir, retorna o tamanho da lista para inserir no final
        return len(self.abertos)

    def estaAberto(self, node):
        """
            Verificar se o nodo esta aberto
        """

        # Para cada nodo na lista de abertos
        for estado in self.abertos:
            # Comparar com o estado atual
            if node.comparar(estado):
                return True

        return False

    def estaVisitado(self, node):
        """
            Verificar se o nodo ja foi visitado
        """

        # Para cada nodo na lista de visitados
        for estado in self.visitados:
            # Comparar com o estado atual
            if node.comparar(estado):
                return True

        return False