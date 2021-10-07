from django.db import models
from django.utils import timezone

class DadosGerais(models.Model):
    endereco = models.CharField(max_length=30)
    endereco_numero = models.CharField(max_length=6)
    endereco_complemento = models.CharField(max_length=35,
                                            blank=True,
                                            null=True)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PessoaFisica(models.Model):
    nome_completo = models.CharField(max_length=80)
    apelido = models.CharField(max_length=15,
                               null=True)
    cpf = models.CharField(max_length=15,
                           unique=True,
                           db_index=True)
    rg = models.CharField(max_length=15,
                          unique=True,
                          db_index=True)
    nascimento = models.DateField(null=True)
    
    class Meta:
        abstract = True


class PessoaJuridica(models.Model):
    razao_social = models.CharField(max_length=80)
    nome_fantasia = models.CharField(max_length=80)
    cnpj = models.CharField(max_length=16)

    class Meta:
        abstract = True


class Cliente(PessoaFisica, PessoaJuridica, DadosGerais):
    TIPO_CLIENTE_CHOICES = [
        ('F', 'Física'),
        ('J', 'Jurídica'),
    ]
    tipo_cliente = models.CharField(max_length=8,
                                    choices=TIPO_CLIENTE_CHOICES,
                                    default='F')
    limite_fiado = models.DecimalField(max_digits=7,
                                       decimal_places=2,
                                       null=True)

    class Meta(PessoaFisica.Meta, PessoaJuridica.Meta, DadosGerais.Meta):
        pass

    def __str__(self):
        return self.nome_completo, self.nome_fantasia


class Fornecedor(PessoaJuridica, PessoaFisica, DadosGerais):
    TIPO_FORNECEDOR_CHOICES = [
        ('F', 'Física'),
        ('J', 'Jurídica'),
    ]
    tipo_fornecedor = models.CharField(max_length=8,
                                       choices=TIPO_FORNECEDOR_CHOICES,
                                       default='J')
    class Meta(PessoaFisica.Meta, PessoaJuridica.Meta, DadosGerais.Meta):
        pass

    def __str__(self):
        return self.nome_completo, self.nome_fantasia