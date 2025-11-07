import unittest
from io import StringIO
from unittest.mock import patch
from calculadora_vol_geo import calculate_area, calculate_volume

class TestCalculadoraVolGeo(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_for_area(self, mock_stdout):
        calculate_area(10.0, 5.0)
        self.assertEqual(mock_stdout.getvalue(), "El área es: 50.0 m2.\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_for_volume(self, mock_stdout):
        calculate_volume(10.0, 5.0, 2.0)
        self.assertEqual(mock_stdout.getvalue(), "El volumen es: 100.0 m3.\n")

    # Test diseñado para fallar
    @patch('sys.stdout', new_callable=StringIO)
    def test_for_area_error(self, mock_stdout):
        calculate_area(5.0, 5.0)
        # Falla porque el resultado esperado no coincide
        self.assertEqual(mock_stdout.getvalue(), "El área es: 30.0 m2.\n")


if __name__ == '__main__':
    unittest.main()
