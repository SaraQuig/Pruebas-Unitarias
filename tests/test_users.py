import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestUserAPI(unittest.TestCase):

    def test_create_user(self):
        response = client.post("/api/users/", json={
            "username": "johndoe",
            "email": "john@example.com",
            "age": 30
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "username": "johndoe",
            "email": "john@example.com",
            "age": 30
        })

    def test_read_users(self):
        response = client.get("/api/users/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_read_user(self):
        response = client.get("/api/users/1")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_update_user(self):
        response = client.put("/api/users/1", json={
            "username": "updatedusername",
            "email": "updated@example.com",
            "age": 35
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "username": "updatedusername",
            "email": "updated@example.com",
            "age": 35
        })

    def test_delete_user(self):
        response = client.delete("/api/users/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "username": "updatedusername",
            "email": "updated@example.com",
            "age": 35
        })
        response = client.get("/api/users/1")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"detail": "User not found"})

if __name__ == '__main__':
    unittest.main()
