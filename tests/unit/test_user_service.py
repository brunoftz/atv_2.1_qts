

from app.services import user_service


def test_should_not_allow_duplicate_users():
    from app.services import user_service

    user_service.users.clear()
    user_service.current_id = 1

    user_service.create_user({"name": "Maylon"})

    user = user_service.create_user({"name": "Maylon"})

    assert user is None


def test_create_user_with_invalid_name():
    user = user_service.create_user({"name": ""})
    assert user is None