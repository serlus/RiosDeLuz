from django.urls import path

from curso.aperitivos.views import video, indice


app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
    path('', indice, name='indice'),
]
