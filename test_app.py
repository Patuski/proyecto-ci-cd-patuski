from app import app

def test_home():
    # Este test solo entra a la web y no mira el texto. 
    # Así podrás cambiar el mensaje en app.py mil veces y siempre funcionará.
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
