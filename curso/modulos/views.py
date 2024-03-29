from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from curso.modulos import facade
from django.http import JsonResponse


def indice(request):
    ctx = {'modulos': facade.listar_modulos_com_aulas()}
    return render(request, 'modulos/indice.html', ctx)


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    aulas = facade.listar_aulas_de_modulo_ordenadas(modulo)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo, 'aulas': aulas})


@login_required
def aula(request, slug):
    aula = facade.encontrar_aula(slug)
    return render(request, 'modulos/aula_detalhe.html', {'aula': aula})

@login_required
def form(request):
    modulos = facade.listar_modulos_ordenados()
    return render(request, 'modulos/modulo_form.html', {'modulos': modulos})

def aula_api(request, slug):
    return JsonResponse({
        'aulas':[{'slug': aula.slug, 'titulo': aula.titulo} for aula in facade.listar_aulas_de_modulo(slug)]
    })