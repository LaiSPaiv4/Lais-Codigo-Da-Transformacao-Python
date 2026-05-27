import unittest

from calculadora import somar_numeros


class TestSomaSimples(unittest.TestCase):

    def test_soma_valores_positivos(self):
        """Valida se a função de soma soma corretamente dois números."""
        resultado = somar_numeros(2, 3)

        # O assertEqual verifica se o resultado é igual ao esperado (5)
        self.assertEqual(resultado, 5)


if __name__ == "__main__":
    unittest.main()