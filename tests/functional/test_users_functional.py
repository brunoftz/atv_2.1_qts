import pytest
from app import create_app
from app.services import user_service

@pytest.fixture
def client():
    app = create_app()
    user_service.users.clear()
    user_service.current_id = 1
    
    return app.test_client()

def test_user_flow(client):
    # 1. Criar usuário
    response = client.post("/users", json={"name": "Maylon"})
    assert response. status_code == 201

    user = response.get_json()
    user_id = user["id"]

    # 2. Buscar usuário
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200

    # 3. Atualizar usuário
    response = client.put(f"/users/{user_id}", json={"name": "Novo Nome"})
    assert response. status_code == 200
    assert response. get_json()["name"] == "Novo Nome"

    # 4. Deletar usuário
    response = client.delete(f"/users/{user_id}")
    assert response. status_code == 204

    # 5. Garantir que foi removido
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 404
    
def test_list_users(client):
    client.post("/users", json={"name": "User1"})
    client.post("/users", json={"name": "User2"})

    response = client.get("/users")

    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 2
    
def test_create_and_list_three_users(client):
    # Criar 3 usuários
    client.post("/users", json={"name": "User1"})
    client.post("/users", json={"name": "User2"})
    client.post("/users", json={"name": "User3"})

    # Listar usuários
    response = client.get("/users")

    # Validar resposta
    assert response.status_code == 200

    users = response.get_json()

    # Validar quantidade
    assert len(users) == 3

    # Validar nomes
    names = [user["name"] for user in users]

    assert "User1" in names
    assert "User2" in names
    assert "User3" in names
    
def test_should_return_400_when_user_already_exists(client):
    client.post("/users", json={"name": "Maylon"})

    response = client.post("/users", json={"name": "Maylon"})

    assert response.status_code == 400