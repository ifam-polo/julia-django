from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    dt_criacao = models.DateField(auto_now_add=True)
    
