from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    # Cambiamos esto para que busque cualquier cosa que empiece por "se ha logrado"
    assert b"se ha logrado" in response.data

