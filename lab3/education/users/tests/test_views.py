from django import urls
from django.contrib.auth import get_user_model
import pytest
from django.db import transaction


@pytest.mark.parametrize('param', ('signup',))
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    response = client.get(temp_url)
    assert response.status_code == 200


@pytest.mark.parametrize('param', (
    'user_course_registration',
    'user_course_list',
    'user_course_detail',
    'user_course_detail_module'))
def test_views(client, param):
    temp_url = urls.reverse(param)
    response = client.get(temp_url)
    assert response.status_code == 301


@pytest.mark.django_db
def test_signup(client, user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    signup_url = urls.reverse(('signup'))
    response = client.post(signup_url, user_data)
    assert user_model.objects.count() == 1
    assert response.status_code == 302


@pytest.mark.django_db
def test_login(client, create_user, user_data):
    user = get_user_model()
    assert user.objects.count() == 1
    url_ = urls.reverse(('login'))
    response = client.post(url_, data=user_data)
    assert response.status_code == 302
    assert response.url == urls.reverse('home')


@pytest.mark.django_db
def test_login(client, create_user, user_data):
    url_ = urls.reverse(('logout'))
    response = client.get(url_)
    assert response.status_code == 302
    assert response.url == urls.reverse('user_course_list')

