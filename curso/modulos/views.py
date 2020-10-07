from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from curso.modulos import facade


def indice(request):
    ctx = {'modulos': facade.listar_modulos_com_aulas()}
    return render(request, 'modulos/indice.html', ctx)


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    aulas = facade.listar_aulas_de_modulo_ordenadas(modulo)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo, 'aulas': aulas})

def tema(request, slug):
    """
    view para demonstração das matérias que esta sendo divulgada.
    """
    tema = facade.encontrar_tema(slug)
    return render(request, 'modulos/tema_detalhe.html', {'tema': tema})


@login_required
def aula(request, slug):
    aula = facade.encontrar_aula(slug)
    return render(request, 'modulos/aula_detalhe.html', {'aula': aula})
