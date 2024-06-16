from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_registrar_cliente():
    response = client.post("/api/clientes/", json={"nombre": "John Doe", "email": "john@example.com"})
    assert response.status_code == 200
    assert response.json() == {"mensaje": "Cliente registrado exitosamente"}

def test_obtener_cliente():
    client.post("/api/clientes/", json={"nombre": "John Doe", "email": "john@example.com"})
    response = client.get("/api/clientes/0")
    assert response.status_code == 200
    assert response.json() == {"nombre": "John Doe", "email": "john@example.com"}

    response = client.get("/api/clientes/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Cliente no encontrado"}
