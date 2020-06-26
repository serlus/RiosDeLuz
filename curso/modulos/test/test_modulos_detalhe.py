from django.urls import reverse
from model_mommy import mommy
import pytest

from curso.django_assertions import assert_contains
from curso.modulos.models import Modulo


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def resp(client, modulo):
    resp = client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))
    return resp


def test_titulos(resp, modulo:Modulo):
    assert_contains(resp, modulo.titulo)


def test_descricao(resp, modulo:Modulo):
    assert_contains(resp, modulo.descricao)

def test_publico(resp, modulo:Modulo):
    assert_contains(resp, modulo.publico)