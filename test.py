from Estado import Estado

def test_comparar():
    primeiro = Estado(matriz=[[1,2,3],[4,5,6],[7,8,9]])
    segundo = Estado(matriz=[[1,2,3],[4,5,6],[7,8,9]])

    print(primeiro.comparar(segundo))

    terceiro = Estado(matriz=[[1,2,3],[4,5,6],[7,9,8]])

    print(terceiro.comparar(primeiro))

test_comparar()