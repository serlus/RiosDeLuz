from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Turma(models.Model):
    """
    classe turma,
    matriculas esta usando get_user_model para herdar o UserModel
    independente de onde esteja, com base no relacionamento muitos
    para muitos (ManyToManyField).
    """
    nome = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    inicio = models.DateField()
    fim = models.DateField()
    matriculas = models.ManyToManyField(get_user_model())
