# Generated by Django 4.1 on 2022-08-21 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0002_alter_articulos_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
