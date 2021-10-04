# Generated by Django 3.2.7 on 2021-10-04 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=30)),
                ('endereco_numero', models.CharField(max_length=6)),
                ('endereco_complemento', models.CharField(max_length=15)),
                ('cidade', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=20)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('atualizado', models.DateTimeField(auto_now=True)),
                ('nome_completo', models.CharField(max_length=80)),
                ('apelido', models.CharField(max_length=15)),
                ('cpf', models.CharField(db_index=True, max_length=15, unique=True)),
                ('rg', models.CharField(db_index=True, max_length=15, unique=True)),
                ('nascimento', models.DateTimeField()),
                ('razao_social', models.CharField(max_length=80)),
                ('nome_fantasia', models.CharField(max_length=80)),
                ('cnpj', models.CharField(max_length=16)),
                ('tipo_fornecedor', models.CharField(choices=[('F', 'Física'), ('J', 'Jurídica')], default='J', max_length=8)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='tipo',
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo_cliente',
            field=models.CharField(choices=[('F', 'Física'), ('J', 'Jurídica')], default='F', max_length=8),
        ),
    ]
