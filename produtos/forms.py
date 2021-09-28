from django.forms import ModelForm, widgets
from .models import Produto

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
            'marca': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Marca',
                'id': 'floatingMarca',
            }),
            'fornecedor': widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Fornecedor',
                'id': 'floatingForn',
            }),
            'disponivel': widgets.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'flexSwDisp',
            })

        }

