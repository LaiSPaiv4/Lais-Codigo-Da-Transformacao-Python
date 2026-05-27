import unittest
from calculadora import Calculadora


class TestCalculadoraExcecoes(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_divisao_por_zero_deve_lancar_erro(self):
        """Verifica se o programa reage corretamente jogando uma exceção ao dividir por zero."""

        # O assertRaises checa se o bloco abaixo vai disparar um ValueError
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)


if __name__ == "__main__":
    unittest.main()