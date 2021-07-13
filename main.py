
from Buscador import Buscador

print("\nInicio do jogo\n\n")

# Pegar tamanho do tabuleiro nos parametros
tamanho = 4
# Pegar estado inicial nos parametros ou gerar
# estadoInicial = [0,1,2,3,4,5,6,7,8]
# estadoInicial = [3,1,2,4,7,5,6,8,0]
estadoInicial = None
# Pegar modo de busca nos parametros
modo = 'profundidade'
# Iniciar buscador
buscador = Buscador(
    tamanho=tamanho,
    estadoInicial=estadoInicial,
    modo=modo
)
# Rodar busca
result = buscador.iniciarBusca()
# Exibir resultados
print("\nResultado:\n")
# print(result)
result.apresentarCaminho()