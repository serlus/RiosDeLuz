from django.urls import reverse
from model_mommy import mommy
import pytest

from curso.django_assertions import assert_contains
from curso.modulos.models import Tema, Modulo


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def temas(modulo):
    return mommy.make(Tema, modulo=modulo)


@pytest.fixture
def resp(client, modulo, temas):
    resp = client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))
    return resp


def test_titulos(resp, tema: Tema):
    assert_contains(resp, tema.titulo)


def test_image(resp, tema: Tema):
    assert_contains(resp, f'src="https://player.vimeo.com/video/{ tema.image_id }"')


def test_modulo_titulos(resp, modulo: Modulo):
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{modulo.titulo}</a></li>')


@pytest.fixture
def resp_sem_usuario(client, tema):
    resp = client.get(reverse('modulos:tema', kwargs={'slug': tema.slug}))
    return resp
