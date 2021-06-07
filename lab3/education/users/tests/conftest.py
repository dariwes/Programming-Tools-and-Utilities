import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def user_data():
    return {
        'username': 'user_name',
        'password': 'user_password123',
        'email': 'test@test.ru',
        'age': '20',
        'is_teacher': True
    }


@pytest.fixture
def create_user(user_data):
    user = get_user_model().objects.create_user(**user_data)
    user.set_password(user_data.get('password'))
    return user


@pytest.fixture
def authenticated_user(client, user_data):
    user = get_user_model().objects.create_user(**user_data)
    user.set_password(user_data.get('password'))
    user.save()
    client.login(**user_data)
    return user
