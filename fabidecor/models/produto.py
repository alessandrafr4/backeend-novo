from django.db import models
from uploader.models import Image
from fabidecor.models import Categoria, Tema

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField(default=0,  null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='produtos')
    tema = models.ForeignKey(Tema, on_delete=models.PROTECT, related_name='temas')
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    Image,
    related_name="+",
    on_delete=models.CASCADE,
    null=True,
    blank=True,
    default=None,

    def __str__(self):
        return f"{self.nome} ({self.quantidade})"
    