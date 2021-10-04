from django.contrib import admin
from .models import Cliente, Fornecedor

@admin.register(Cliente)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome_completo', 'razao_social', 'cpf', 'cnpj', 'atualizado']

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['nome_completo', 'razao_social', 'cpf', 'cnpj', 'atualizado']
    verbose_name = 'Fornecedor'
    verbose_name_plural = 'Fornecedores'