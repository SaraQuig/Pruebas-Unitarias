import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestProductAPI(unittest.TestCase):

    def test_create_product(self):
        response = client.post("/api/products/", json={
            "name_pro": "Product 1",
            "descrip_pro": "Description 1",
            "cant": 10,
            "precio": 99.99,
            "oferta": False
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "id_pro": 1,
            "name_pro": "Product 1",
            "descrip_pro": "Description 1",
            "cant": 10,
            "precio": 99.99,
            "oferta": False
        })

    def test_read_products(self):
        response = client.get("/api/products/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_read_product(self):
        response = client.get("/api/products/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_update_product(self):
        response = client.put("/api/products/1", json={
            "name_pro": "Updated Product",
            "descrip_pro": "Updated Description",
            "cant": 20,
            "precio": 79.99,
            "oferta": True
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "id_pro": 1,
            "name_pro": "Updated Product",
            "descrip_pro": "Updated Description",
            "cant": 20,
            "precio": 79.99,
            "oferta": True
        })

    def test_delete_product(self):
        response = client.delete("/api/products/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "id_pro": 1,
            "name_pro": "Updated Product",
            "descrip_pro": "Updated Description",
            "cant": 20,
            "precio": 79.99,
            "oferta": True
        })
        response = client.get("/api/products/1")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"detail": "Product not found"})

#Pruebas unitarias utilizando unittest
if __name__ == '__main__':
    unittest.main()
