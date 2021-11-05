from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# testar login com usuario invalido
def test_sign_in_with_invalid_user():
    response = client.post('/sign-in', json={ 'email': 'test111@test.com', 'password': 'test@test' })
    assert response.json() == { "status": "error", "message": "EMAIL_NOT_FOUND" }

# testar login com usuario valido
def test_sign_in_with_valid_user():
    response = client.post('/sign-in', json={ 'email': 'test@test.com', 'password': 'teste@123' })
    assert response.status_code == 200

# testar verificacao de token
def test_verification():
    response = client.post('/verification', json={ 'idToken': 'umtokentesteaquihueheu' })
    assert response.status_code == 200

