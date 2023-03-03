from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    dt_criacao = models.DateField(auto_now_add=True)

class Transacao(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    obs = models.TextField()
    
    class Meta: 
        verbose_name_plural = 'Transacoes'
