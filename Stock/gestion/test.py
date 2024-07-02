# test.py

import unittest
from .models import Producto

class ProductoTestCase(unittest.TestCase):

    def setUp(self):
        self.producto = Producto.objects.create(nombre='Producto de prueba', cantidad=10)

    def test_nombre_producto(self):
        self.assertEqual(str(self.producto), 'Producto de prueba')

    def test_actualizacion_inventario(self):
        self.producto.cantidad = 5
        self.producto.save()
        self.assertEqual(self.producto.cantidad, 5)
