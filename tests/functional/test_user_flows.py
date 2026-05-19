import pytest


@pytest.mark.functional
def test_complete_user_lifecycle(client):
    create_resp = client.post("/users", json={"name": "Lifecycle"})
    user_id = create_resp.get_json()["id"]

    get_resp = client.get(f"/users/{user_id}")
    assert get_resp.get_json()["name"] == "Lifecycle"

    update_resp = client.put(f"/users/{user_id}", json={"name": "Atualizado"})
    assert update_resp.get_json()["name"] == "Atualizado"

    delete_resp = client.delete(f"/users/{user_id}")
    assert delete_resp.status_code == 204

    not_found = client.get(f"/users/{user_id}")
    assert not_found.status_code == 404


@pytest.mark.functional
def test_multiple_users_can_be_created_and_listed(client):
    client.post("/users", json={"name": "User A"})
    client.post("/users", json={"name": "User B"})
    client.post("/users", json={"name": "User C"})

    response = client.get("/users")
    names = {user["name"] for user in response.get_json()}
    assert names == {"User A", "User B", "User C"}


@pytest.mark.functional
def test_delete_user_then_list_excludes_deleted(client):
    client.post("/users", json={"name": "Manter"})
    client.post("/users", json={"name": "Remover"})
    client.delete("/users/2")

    response = client.get("/users")
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["name"] == "Manter"
