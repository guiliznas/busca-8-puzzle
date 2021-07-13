import unittest
from Estado import Estado

class Teste(unittest.TestCase):
    def test_comparar(self):
        primeiro = Estado(matriz=[[1,2,3],[4,5,6],[7,8,9]])
        segundo = Estado(matriz=[[1,2,3],[4,5,6],[7,8,9]])

        self.assertEqual(primeiro.comparar(segundo), True)

        terceiro = Estado(matriz=[[1,2,3],[4,5,6],[7,9,8]])
        
        self.assertEqual(terceiro.comparar(primeiro), False)

if __name__ == '__main__':
    unittest.main()