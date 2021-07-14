import time
import argparse
from Buscador import Buscador
from utils import MODO_CUSTO_UNIFORME, MODO_A_SIMPLES, MODO_A_MELHORADO, MODO_A_INVERSOES

# Declaracoes dos atributos aceitos
parser = argparse.ArgumentParser()
parser.add_argument(
    "--modo",
    help="Metodo de busca a ser considerado",
    choices=[MODO_CUSTO_UNIFORME, MODO_A_SIMPLES, MODO_A_MELHORADO, MODO_A_INVERSOES],
    type=str,
    default=MODO_A_MELHORADO,
)
parser.add_argument(
    '--tamanho',
    help="Dimensao do tabuleiro. Informar quantidade de linhas, padrao = 3.",
    type=int,
    default=4,
)
parser.add_argument(
    "--inicial",
    help="Lista para indicar o estado inicial.\nConsiderar a ordem de leitura natural, com os numeros separados por virgula.\nEx: 1,2,3,4,5,6,7,8,0 para o resultado padrao.",
)
parser.add_argument(
    "--objetivo",
    help="Lista para indicar o estado objetivo.\nConsiderar a ordem de leitura natural, com os numeros separados por virgula.\nEx: 1,2,3,4,5,6,7,8,0 para o resultado padrao.",
)
args = parser.parse_args()

# Pegar tamanho do tabuleiro nos parametros
tamanho = args.tamanho

# Pegar estado inicial nos parametros
estadoInicial = None
# estadoInicial = [1,2,3,4,5,6,0,7,8] # 3 - 0s
# estadoInicial = [2,0,3,1,5,6,4,7,8] # 6 - 0s
# estadoInicial = [1,3,5,4,6,2,8,7,0] # 18
# estadoInicial = [3,1,2,4,7,5,6,8,0] # 22 - 2s
# estadoInicial = [1,2,5,3,0,4,6,7,8] # 22 - 3s
# estadoInicial = [7,5,3,4,1,8,2,0,6] # 25 - 35s
# estadoInicial = [4,7,5,0,2,1,3,6,8] # 27 - 67s

estadoInicial = [1,2,3,4,5,6,7,8,9,10,11,12,13,0,14,15] # Exemplo para 4x4

if args.inicial:
    estadoInicial = [int(val) for val in args.inicial.split(',')]

# Pegar o objetivo nos parametros
objetivo = args.objetivo

# Pegar modo de busca nos parametros
modo = args.modo

# Iniciar buscador
buscador = Buscador(
    tamanho=tamanho,
    estadoInicial=estadoInicial,
    modo=modo,
    objetivo=objetivo,
)

print("\nInicio do jogo\n\n")
inicio = time.time()
# Rodar busca
result = buscador.iniciarBusca()
final = time.time()

# Exibir resultados
print("\nResultado:\n")
tamanhoCaminho = result.apresentarCaminho()

print("Expandidos: {}".format(buscador.expandidos))
print("Criados: {}".format(buscador.criados))
print("Maior fronteira encontrada: {}".format(buscador.max_abertos))
print("Tamanho do caminho: {}".format(tamanhoCaminho))
print("Tempo percorrido: {:.2f} segundos".format(final - inicio))