import pytest
from curso.django_assertions import assert_contains
from django.urls import reverse


@pytest.fixture
def resp(client):
    resp = client.get(reverse('home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Rios de Luz</title>')


def test_description(resp):
    assert_contains(resp, '<meta name="description" content="página do curso Rios de Luz">')


def test_author(resp):
    assert_contains(resp, '<meta name="author" content="Sergio Casas">')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("home")}">Rios de Luz</a>')
