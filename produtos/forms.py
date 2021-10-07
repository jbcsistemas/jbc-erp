from django.forms import ModelForm, widgets
from .models import Categoria, Marca, Produto

class RegistroCategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        exclude = ('slug',)
        widgets = {
            'nome': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome',
                'id': 'floatingNome',
            }),
            'fornecedores': widgets.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Fornecedores',
                'id': 'floatingFornecedor',
            })
        }


class RegistroMarcaForm(ModelForm):
    class Meta:
        model = Marca
        exclude = ('slug',)
        widgets = {
            'nome': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome',
                'id': 'floatingNome',
            }),
            'categoria': widgets.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Categoria',
                'id': 'floatingCategoria',
            }),
            'fornecedores': widgets.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Fornecedores',
                'id': 'floatingFornecedores',
            })
        }


class RegistroProdutosForm(ModelForm):
    class Meta:
        model = Produto
        exclude = ('slug',)
        widgets = {
            'codigo_barras': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Código de Barras',
                'id': 'floatingBarras',
            }),
            'nome': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do Produto',
                'id': 'floatingNome',
            }),
            'descricacao': widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descrição do Produto',
                'id': 'floatingDesc',
                'style': 'height: 100px',
            }),
            'custo': widgets.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Custo',
                'id': 'floatingCusto',
            }),
            'preco': widgets.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Preço',
                'id': 'floatingPreco',
            }),
            'categoria': widgets.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Categoria',
                'id': 'floatingCate',
            }),
            'marca': widgets.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Marca',
                'id': 'floatingMarca',
            }),
            'fornecedores': widgets.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Fornecedores',
                'id': 'floatingForn',
            }),
            'disponivel': widgets.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'flexSwDisp',
            })

        }

