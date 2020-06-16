from curso.django_assertions import assert_contains
from django.test import Client


def test_status_code(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200

def test_title(client: Client):
    resp = client.get('/')
    assert_contains(resp, '<title>Rios de Luz</title>')

def test_description(client: Client):
    resp = client.get('/')
    assert_contains(resp, '<meta name="description" content="Source code generated using layoutit.com">')

def test_author(client: Client):
    resp = client.get('/')
    assert_contains(resp, '<meta name="author" content="LayoutIt!">')

def test_navbar_brand(client: Client):
    resp = client.get('/')
    assert_contains(resp, '<a class="navbar-brand" href="#">Navbar</a>')

def test_nav_link_home(client: Client):
    resp = client.get('/')
    assert_contains(resp, '<a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>')
