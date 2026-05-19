import pytest

from app.services import user_service


@pytest.mark.unit
def test_get_all_users_returns_empty_list_initially():
    assert user_service.get_all_users() == []


@pytest.mark.unit
def test_create_user_assigns_incremental_id():
    user = user_service.create_user({"name": "Ana"})
    assert user["id"] == 1
    second = user_service.create_user({"name": "Bob"})
    assert second["id"] == 2


@pytest.mark.unit
def test_create_user_stores_name_correctly():
    user = user_service.create_user({"name": "Carlos"})
    assert user["name"] == "Carlos"


@pytest.mark.unit
def test_get_user_by_id_returns_user_when_exists():
    created = user_service.create_user({"name": "Diana"})
    found = user_service.get_user_by_id(created["id"])
    assert found == created


@pytest.mark.unit
def test_get_user_by_id_returns_none_when_not_found():
    assert user_service.get_user_by_id(999) is None


@pytest.mark.unit
def test_update_user_returns_none_when_not_found():
    result = user_service.update_user(404, {"name": "X"})
    assert result is None


@pytest.mark.unit
def test_update_user_updates_existing_user():
    created = user_service.create_user({"name": "Eva"})
    updated = user_service.update_user(created["id"], {"name": "Eva Silva"})
    assert updated["name"] == "Eva Silva"


@pytest.mark.unit
def test_delete_user_removes_user_from_list():
    created = user_service.create_user({"name": "Fabio"})
    user_service.delete_user(created["id"])
    assert user_service.get_user_by_id(created["id"]) is None


@pytest.mark.unit
def test_count_users_returns_zero_when_empty():
    assert user_service.count_users() == 0


@pytest.mark.unit
def test_count_users_returns_correct_number():
    user_service.create_user({"name": "Gabi"})
    user_service.create_user({"name": "Hugo"})
    assert user_service.count_users() == 2
    
@pytest.mark.unit
def test_create_user_with_invalid_name():
    user = user_service.create_user({"name": ""})
    assert user is None
