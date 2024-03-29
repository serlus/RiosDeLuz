from typing import List

from django.db.models.query import Prefetch

from curso.modulos.models import Aula, Modulo


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos, ordenados por títulos
    :return:
    """
    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)


def listar_aulas_de_modulo_ordenadas(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())


def encontrar_aula(slug):
    return Aula.objects.select_related('modulo').get(slug=slug)


def listar_modulos_com_aulas():
    """
    Lista as aulas e modulos ordenadas.
    """
    aulas_ordenadas = Aula.objects.order_by('order')
    return Modulo.objects.order_by('order').prefetch_related(
        Prefetch('aula_set', queryset=aulas_ordenadas, to_attr='aulas')
        ).all()

def listar_aulas_de_modulo(modulo_slug):
    """
    Lista as aulas e modulos ordenadas.
    """
    return Aula.objects.filter(modulo__slug=modulo_slug).order_by('order').all()
    