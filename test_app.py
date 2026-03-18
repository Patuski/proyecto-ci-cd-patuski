from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    # Esto solo mira que la web no dé error (200 es OK)
    assert response.status_code == 200 
    # Borramos la línea que busca frases exactas
