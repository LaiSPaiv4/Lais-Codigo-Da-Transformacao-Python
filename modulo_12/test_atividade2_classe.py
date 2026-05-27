import unittest
from calculadora import Calculadora


class TestClasseCalculadora(unittest.TestCase):

    def setUp(self):
        """Roda antes de cada teste, preparando a calculadora."""
        self.calc = Calculadora()

    def test_metodo_somar(self):
        """Testa o método somar da classe Calculadora."""
        self.assertEqual(self.calc.somar(10, 5), 15)
        self.assertEqual(self.calc.somar(-1, 1), 0)

    def test_metodo_dividir(self):
        """Testa o método dividir com valores válidos."""
        self.assertEqual(self.calc.dividir(10, 2), 5.0)


if __name__ == "__main__":
    unittest.main()