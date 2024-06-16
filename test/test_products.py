from fastapi.testclient import TestClient
from main import app

# Crear un cliente de prueba
client = TestClient(app)

def test_create_product():
    response = client.post("/api/products/", json={
        "name_pro": "Product 1",
        "descrip_pro": "Description 1",
        "cant": 10,
        "precio": 99.99,
        "oferta": False
    })
    assert response.status_code == 200
    assert response.json() == {
        "id_pro": 1,
        "name_pro": "Product 1",
        "descrip_pro": "Description 1",
        "cant": 10,
        "precio": 99.99,
        "oferta": False
    }

def test_read_products():
    response = client.get("/api/products/")
    assert response.status_code == 200
    assert response.json() == [{
        "id_pro": 1,
        "name_pro": "Product 1",
        "descrip_pro": "Description 1",
        "cant": 10,
        "precio": 99.99,
        "oferta": False
    }]

def test_read_product():
    response = client.get("/api/products/1")
    assert response.status_code == 200
    assert response.json() == {
        "id_pro": 1,
        "name_pro": "Product 1",
        "descrip_pro": "Description 1",
        "cant": 10,
        "precio": 99.99,
        "oferta": False
    }

def test_update_product():
    response = client.put("/api/products/1", json={
        "name_pro": "Updated Product",
        "descrip_pro": "Updated Description",
        "cant": 20,
        "precio": 79.99,
        "oferta": True
    })
    assert response.status_code == 200
    assert response.json() == {
        "id_pro": 1,
        "name_pro": "Updated Product",
        "descrip_pro": "Updated Description",
        "cant": 20,
        "precio": 79.99,
        "oferta": True
    }

def test_delete_product():
    response = client.delete("/api/products/1")
    assert response.status_code == 200
    assert response.json() == {
        "id_pro": 1,
        "name_pro": "Updated Product",
        "descrip_pro": "Updated Description",
        "cant": 20,
        "precio": 79.99,
        "oferta": True
    }

    response = client.get("/api/products/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}
