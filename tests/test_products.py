import sys
import os
from fastapi.testclient import TestClient

# Añadir la ruta del directorio raíz de tu proyecto al path de Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Importar la aplicación FastAPI desde main.py después de añadir la ruta al path
from app.main import app # type: ignore
# Crear un cliente de prueba
client = TestClient(app)

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocFileSuite('/app/api/endpoints/products.py'))
    return tests

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

#pruebas unitarias
if __name__ == "__main__":
    import doctest
    doctest.testmod()