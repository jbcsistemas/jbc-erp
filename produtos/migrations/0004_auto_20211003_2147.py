# Generated by Django 3.2.7 on 2021-10-04 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0002_auto_20211003_2146'),
        ('produtos', '0003_auto_20211003_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='fornecedores',
            field=models.ManyToManyField(related_name='categorias', to='pessoas.Fornecedor'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='fornecedores',
            field=models.ManyToManyField(related_name='marcas', to='pessoas.Fornecedor'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='fornecedores',
            field=models.ManyToManyField(related_name='produtos', to='pessoas.Fornecedor'),
        ),
    ]
