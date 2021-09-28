from django.contrib import admin
from .models import Categoria, Marca, Produto

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    prepopulated_fields = {'slug': ('nome',)}


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    prepopulated_fields = {'slug': ('nome',)}


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'codigo_barras', 'nome',
                    'custo', 'preco', 'categoria',
                    'disponivel', 'atualizado']
    list_filter = ['disponivel', 'criado', 'atualizado']
    list_editable = ['custo', 'preco', 'disponivel']
    prepopulated_fields = {'slug': ('codigo_barras',)}