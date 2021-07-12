from Estado import Estado
import random

class Buscador:
    def __init__(self, tamanho=3, estadoInicial=None, modo=None):

        self.tamanho = tamanho
        if estadoInicial is None:
            print("Gerando estado inicial")
            estadoInicial = list(range(tamanho*tamanho))
            random.shuffle(estadoInicial)

        matriz = []
        while(len(estadoInicial) > 0):
            matriz.append(estadoInicial[:tamanho])
            estadoInicial = estadoInicial[tamanho:]

        nodo = Estado(matriz=matriz)
        print(nodo)

        self.visitados = []
        self.abertos = [nodo]

        return

    def iniciarBusca(self):

        count = 0
        while count < 100:
            count += 1
            # loop
            if len(self.abertos) == 0:
                return None
            # pega o primeiro nodo da lista de abertos
            nodo = self.abertos.pop(0)
            print("Testando:\n{}".format(nodo))
            # adiciona nos visitados
            self.visitados.append(nodo)
            # verifica se  eh objetivo
            ehObjetivo = nodo.ehObjetivo()
            # print("Eh objetivo: {}".format(ehObjetivo))
            if ehObjetivo:
                return nodo
            # Se nao for, joga ele para os visitados
            # Pega os filhos dele e adiciona nos abertos
            filhos = nodo.filhos(tamanho=self.tamanho)
            # print("{} filhos".format(len(filhos)))
            if len(filhos) > 0:
                self._inserirNodoAberto(estados=filhos)

            #   Verificacoes para inserir nos abertos
            # Quando encontrar o objetivo para o loop
            # Retorna resultados

        print("\n\n\nabertos\n")
        for aberto in self.abertos[5:]:
            print(aberto)
        print("\nabertos\n\n\n")

        return nodo

    def _inserirNodoAberto(self, estados=[]):

        for estado in estados:
            if self.estaVisitado(estado):
                # print("Ja foi visitado")
                pass
            else:
                if self.estaAberto(estado):
                    # print("Ja esta aberto")
                    pass
                else:
                    print(estado)
                    pos = self.__pegarPosicao(estado=estado)
                    self.abertos.insert(pos, estado)

        return

    def __pegarPosicao(self, estado=None):

        for ind, nodo in enumerate(self.abertos):
            # print(nodo.heuristica, estado.heuristica)
            if nodo.heuristica > estado.heuristica:
                # print("Nodo: {} - Estado: {}".format(nodo.heuristica, estado.heuristica))
                return ind

        return len(self.abertos)

    def estaAberto(self, node):
        # Verificar se a heuristica eh menor

        for estado in self.abertos:
            if node.comparar(estado):
                return True

        return False

    def estaVisitado(self, node):

        for estado in self.visitados:
            if node.comparar(estado):
                return True

        return False

    def apresentarNodos(self, nodos):
        for item in nodos:
            print(item.matriz)
        return