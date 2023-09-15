from django.db import models

class Tema(models.Model):
    nome = models.CharField(max_length=255)
   
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tema"
        verbose_name_plural = "Temas"

