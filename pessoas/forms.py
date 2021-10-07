from django.forms import ModelForm, widgets, DateInput
from .models import Cliente, Fornecedor

class RegistroClienteForm(ModelForm):
    class Meta:
        model = Cliente
        exclude = ('slug',)
        widgets = {
            'nome_completo': widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Nome completo',
                'id': 'floatingNomeCompleto',
                'required': '',
            }),
            'apelido': widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Apelido',
                'id': 'floatingApelido',
            }),
            'cpf': widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'CPF',
                'id': 'floatingCPF',
            }),
            'rg': widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'RG',
                'id': 'floatingRG',
            }),
            'nascimento': widgets.DateInput(format="%d/%m/%y", attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Nascimento dd/mm/aaaa',
                'id': 'floatingNascimento',
            }),
            'razao_social': widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Razão Social',
                'id': 'floatingRSocial',
            }),
            'nome_fantasia': widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Nome Fantasia',
                'id': 'floatingNFantasia',
            }),
            'cnpj': widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'CNPJ',
                'id': 'floatingCNPJ',
            }),
            'endereco': widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Endereço',
                'id': 'floatingEndereco',
            }),
            'endereco_numero': widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Número',
                'id': 'floatingNumero',
            }),
            'endereco_complemento': widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Complemento',
                'id': 'floatingComplemento',
            }),
            'cidade': widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Cidade',
                'id': 'floatingCidade',
            }),
            'estado': widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Estado',
                'id': 'floatingEstado',
            }),
            'limite_fiado': widgets.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Limite',
                'id': 'floatingLimite',
            })
        }


class RegistroFornecedorForm(ModelForm):
    class Meta:
       model = Fornecedor
       exclude = ('slug',)
       widgets = {
           'nome_completo': widgets.Textarea(attrs={
               'class': 'form-control',
               'placeholder': 'Nome completo',
               'id': 'floatingNomeCompleto',
               'required': '',
           }),
           'apelido': widgets.Textarea(attrs={
               'class': 'form-control',
               'placeholder': 'Apelido',
               'id': 'floatingApelido',
           }),
           'cpf': widgets.Textarea(attrs={
               'class': 'form-control',
               'placeholder': 'CPF',
               'id': 'floatingCPF',
           }),
           'rg': widgets.Textarea(attrs={
               'class': 'form-control',
               'placeholder': 'RG',
               'id': 'floatingRG',
           }),
           'nascimento': widgets.DateInput(format="%d/%m/%y", attrs={
               'type': 'date',
               'class': 'form-control',
               'placeholder': 'Nascimento dd/mm/aaaa',
               'id': 'floatingNascimento',
           }),
           'razao_social': widgets.Textarea(attrs={
               'class': 'form-control',
               'placeholder': 'Razão Social',
               'id': 'floatingRSocial',
           }),
           'nome_fantasia': widgets.Textarea(attrs={
               'class': 'form-control',
               'placeholder': 'Nome Fantasia',
               'id': 'floatingNFantasia',
           }),
           'cnpj': widgets.Textarea(attrs={
               'class': 'form-control',
               'placeholder': 'CNPJ',
               'id': 'floatingCNPJ',
           }),
           'endereco': widgets.Textarea(attrs={
               'class': 'form-control',
               'placeholder': 'Endereço',
               'id': 'floatingEndereco',
           }),
           'endereco_numero': widgets.Textarea(attrs={
               'class': 'form-control',
               'placeholder': 'Número',
               'id': 'floatingNumero',
           }),
           'endereco_complemento': widgets.Textarea(attrs={
               'class': 'form-control',
               'placeholder': 'Complemento',
               'id': 'floatingComplemento',
           }),
           'cidade': widgets.Textarea(attrs={
               'class': 'form-control',
               'placeholder': 'Cidade',
               'id': 'floatingCidade',
           }),
           'estado': widgets.Textarea(attrs={
               'class': 'form-control',
               'placeholder': 'Estado',
               'id': 'floatingEstado',
           }),
           'limite_fiado': widgets.NumberInput(attrs={
               'class': 'form-control',
               'placeholder': 'Limite',
               'id': 'floatingLimite',
           })
       }