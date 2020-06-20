import pytest
from curso.django_assertions import assert_contains
from django.urls import reverse


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Rios de Luz - Home</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Rios de Luz</a>')


def test_email_link(resp):
    assert_contains(resp, 'href="mailto:contato@riosdeluz.brisaverde.life"')
