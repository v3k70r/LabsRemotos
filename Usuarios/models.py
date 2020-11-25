from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Usuario(AbstractUser):
    es_mentor = models.BooleanField(default=False)
    es_admin = models.BooleanField(default=False)


class Entrada(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True, editable=False)
    autor = models.ForeignKey(Usuario, default = 1, on_delete = models.CASCADE)


class Banner(models.Model):
    titulo = models.TextField(max_length=200, default="Título.")
    imagen = models.ImageField(upload_to='media/banner/', default='media/banner/banner.png')
    descripcion = models.TextField(max_length=200, default="Descripción.")