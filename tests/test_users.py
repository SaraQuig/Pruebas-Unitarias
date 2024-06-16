import unittest
import json
import sys
import os
from flask import Flask
from app.api.endpoints.users import users_bp

# Obtener la ruta al directorio principal del proyecto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Añadir la ruta al directorio principal del proyecto al sys.path
sys.path.insert(0, project_root)
import unittest
import requests

class TestUsersAPI(unittest.TestCase):

    base_url = 'http://localhost:5000'  # Asegúrate de que esta URL sea correcta

    def test_register_user(self):
        user_data = {
            'nombre': 'John',
            'apellido': 'Doe',
            'correo': 'john.doe@example.com',
            'cedula': '1234567890',
            'celular': '987654321'
        }

        try:
            response = requests.post(f'{self.base_url}/users/register', json=user_data)
            self.assertEqual(response.status_code, 201)
            self.assertIn("Usuario registrado correctamente", response.json().get('message'))
        except requests.exceptions.ConnectionError as e:
            self.fail(f"Error de conexión al intentar realizar la solicitud: {e}")

if __name__ == '__main__':
    unittest.main()

