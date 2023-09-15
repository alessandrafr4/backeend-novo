from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    

class Tema(models.Model):
    nome = models.CharField(max_length=255)
   
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tema"
        verbose_name_plural = "Temas"


class Produto(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0,  null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    tema = models.ManyToManyField(Tema, related_name="produto")

    
    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"
    
