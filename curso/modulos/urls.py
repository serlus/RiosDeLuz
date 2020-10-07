from django.urls import path

from curso.modulos import views


app_name = 'modulos'
urlpatterns = [
    path('<slug:slug>', views.detalhe, name='detalhe'),
    path('aulas/<slug:slug>', views.aula, name='aula'),
    path('temas/<slug:slug>', views.tema, name='tema'),
    path('', views.indice, name='indice'),
]
