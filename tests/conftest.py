import pytest

import app.services.user_service as user_service
from app import create_app


@pytest.fixture(autouse=True)
def reset_users():
    user_service.users.clear()
    user_service.current_id = 1
    yield
    user_service.users.clear()
    user_service.current_id = 1


@pytest.fixture
def client():
    app = create_app()
    return app.test_client()
