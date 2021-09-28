from django.db import models
from django.urls import reverse

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=15,
                            unique=True)
    slug = models.SlugField(max_length=100,
                            unique=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome


class Marca(models.Model):
    nome = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categoria,
                                  related_name='marcas',
                                  on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'


class Produto(models.Model):
    codigo_barras = models.CharField(max_length=14,
                                     db_index=True)
    nome = models.CharField(max_length=100)
    descricacao = models.TextField(verbose_name="descrição",
                                   blank=True)
    custo = models.DecimalField(max_digits=10,
                                decimal_places=2)
    preco = models.DecimalField(verbose_name="preço",
                                max_digits=10,
                                decimal_places=2)
    slug = models.SlugField(max_length=100,
                            db_index=True)
    categoria = models.ForeignKey(Categoria,
                                  related_name='produtos',
                                  on_delete=models.CASCADE)
    marca = models.CharField(max_length=15) # receberá uma chave estrangeira
    fornecedor = models.CharField(max_length=15) # situação de 'marca'
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    disponivel = models.BooleanField(default=True)

    class Meta:
        ordering = ('nome',)
        index_together = (('id', 'codigo_barras', 'slug'),)

    def __str__(self):
        return self.nome.upper()

    def get_absolute_url(self):
        return reverse('produtos:detalhes',
                       args=[self.pk])
