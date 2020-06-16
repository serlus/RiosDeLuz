from curso.django_assertions import assert_contains
from django.test import Client


def test_status_code(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200

def test_status_code(client: Client):
    resp = client.get('/')
    assert_contains(resp, '<title>Rios de Luz</title>')

def test_status_code(client: Client):
    resp = client.get('/')
    assert_contains(resp, '<meta name="description" content="Source code generated using layoutit.com">')

def test_status_code(client: Client):
    resp = client.get('/')
    assert_contains(resp, '<meta name="author" content="LayoutIt!">')

def test_status_code(client: Client):
    resp = client.get('/')
    assert_contains(resp, '<a class="navbar-brand" href="#">Navbar</a>')

def test_status_code(client: Client):
    resp = client.get('/')
    assert_contains(resp, '<a class="navbar-brand" href="#">Navbar</a>')
