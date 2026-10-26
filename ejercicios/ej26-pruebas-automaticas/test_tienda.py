# Ej26 · test_tienda.py · Pruebas unitarias de tienda.py
import unittest

from tienda import aplicar_descuento, precio_con_iva


class TestTienda(unittest.TestCase):

    # Ejemplo hecho: cada prueba es un método que empieza por "test_".
    # assertEqual(obtenido, esperado) falla si los dos valores no son iguales.
    def test_iva_general(self):
        self.assertEqual(precio_con_iva(100), 121.0)

    # PASO 2: prueba que precio_con_iva(100, "reducido") es 110.0
    #     def test_iva_reducido(self):
    #         ...


    # PASO 3: prueba que precio_con_iva(50, "superreducido") es 52.0


    # PASO 4: prueba que aplicar_descuento(80, 20) es 64.0   (un 20 % menos)
    #         Llama al método test_descuento_del_20


    # PASO 5: prueba que aplicar_descuento(80, 0) es 80.0    (sin descuento)
    #         Llama al método test_descuento_cero


    # PASO 6: prueba que aplicar_descuento(80, 150) lanza ValueError:
    #     def test_descuento_no_valido(self):
    #         with self.assertRaises(ValueError):
    #             aplicar_descuento(80, 150)


if __name__ == "__main__":
    unittest.main()
