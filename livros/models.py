from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.categoria


class Livro(models.Model):
    nome = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    autor = models.CharField(max_length=30)
    em_estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome

    def disponivel(self):
        return bool(self.em_estoque)