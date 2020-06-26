from django.shortcuts import render
from curso.modulos import facade


# Create your views here.
def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo})
