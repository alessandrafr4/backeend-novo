from django.db import models
from uploader.models import Image

class Tema(models.Model):
    nome = models.CharField(max_length=255)
    Image,
    related_name="+",
    on_delete=models.CASCADE,
    null=True,
    blank=True,
    default=None,
   
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tema"
        verbose_name_plural = "Temas"

