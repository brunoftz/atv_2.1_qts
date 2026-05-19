import pytest


@pytest.mark.integration
def test_get_users_empty_list(client):
    response = client.get("/users")
    assert response.status_code == 200
    assert response.get_json() == []


@pytest.mark.integration
def test_post_then_get_list_contains_user(client):
    client.post("/users", json={"name": "Integracao"})
    response = client.get("/users")
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["name"] == "Integracao"


@pytest.mark.integration
def test_put_user_not_found_returns_404(client):
    response = client.put("/users/999", json={"name": "Ninguem"})
    assert response.status_code == 404
    assert response.get_json()["error"] == "User not found"


@pytest.mark.integration
def test_post_without_name_returns_400(client):
    response = client.post("/users", json={})
    assert response.status_code == 400
    assert "name is required" in response.get_json()["error"]


@pytest.mark.integration
def test_get_users_count_returns_json(client):
    client.post("/users", json={"name": "Contagem"})
    client.post("/users", json={"name": "Contagem 2"})
    response = client.get("/users/count")
    assert response.status_code == 200
    assert response.get_json() == {"count": 2}
