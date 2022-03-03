from django.db import models
from datetime import datetime 
from django.conf import settings

# Create your models here.

class Receita(models.Model):
    nome = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    publicada = models.BooleanField(default=False)


    