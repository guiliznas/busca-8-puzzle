import argparse
from Buscador import Buscador
from utils import MODO_CUSTO_UNIFORME, MODO_A_SIMPLES, MODO_A_MELHORADO

# Declaracoes dos atributos aceitos
parser = argparse.ArgumentParser()
parser.add_argument(
    "--modo",
    help="Metodo de busca a ser considerado",
    choices=[MODO_CUSTO_UNIFORME, MODO_A_SIMPLES, MODO_A_MELHORADO],
    type=str,
)
parser.add_argument(
    '--tamanho',
    help="Dimensao do tabuleiro. Informar quantidade de linhas, padrao = 3.",
    type=int,
    default=3,
)
parser.add_argument(
    "--inicial",
    help="Lista para indicar o estado inicial.\nConsiderar a ordem de leitura natural, com os numeros separados por virgula.\nEx: 1,2,3,4,5,6,7,8,0 para o resultado padrao.",
)
args = parser.parse_args()

# Pegar tamanho do tabuleiro nos parametros
tamanho = args.tamanho

# Pegar estado inicial nos parametros ou gerar
# estadoInicial = [0,1,2,3,4,5,6,7,8]
# estadoInicial = [3,1,2,4,7,5,6,8,0]
estadoInicial = None
if args.inicial:
    estadoInicial = [int(val) for val in args.inicial.split(',')]

# Pegar modo de busca nos parametros
modo = args.modo or MODO_A_MELHORADO
# Iniciar buscador
buscador = Buscador(
    tamanho=tamanho,
    estadoInicial=estadoInicial,
    modo=modo
)
print("\nInicio do jogo\n\n")
# Rodar busca
result = buscador.iniciarBusca()
# Exibir resultados
print("\nResultado:\n")
# print(result)
tamanhoCaminho = result.apresentarCaminho()

print("Expandidos: {}".format(buscador.expandidos))
print("Criados: {}".format(buscador.criados))
print("Maximo abertos simultaneamente: {}".format(buscador.max_abertos))
print("Tamanho do caminho: {}".format(tamanhoCaminho))