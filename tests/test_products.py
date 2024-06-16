import unittest
import json
from flask import Flask
from app.api.endpoints.products import products_bp

class TestProductsAPI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(products_bp)
        self.client = self.app.test_client()

    def test_add_product(self):
        # Test de agregar producto exitoso
        data = {
            "nombre": "Producto 1",
            "precio": 100.0,
            "descripcion": "Descripción del producto 1"
        }

        response = self.client.post('/add', json=data)
        self.assertEqual(response.status_code, 201)
        # Verificar si la respuesta es un JSON válido
        data = json.loads(response.data.decode('utf-8'))

        # Verificar si el mensaje esperado está en la respuesta
        self.assertIn("Producto añadido correctamente", data['message'])

        # Test de agregar producto con campos faltantes
        data_incompleta = {
            "nombre": "Producto 2",
            "descripcion": "Descripción del producto 2"
            # Falta precio
        }

        response_incompleta = self.client.post('/add', json=data_incompleta)
        self.assertEqual(response_incompleta.status_code, 400)
        self.assertIn(b"error", response_incompleta.data)

if __name__ == '__main__':
    unittest.main()
