# Generated by Django 3.2 on 2021-05-14 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(max_length=150, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='client',
            name='firstName',
            field=models.CharField(max_length=60, verbose_name='firstName'),
        ),
        migrations.AlterField(
            model_name='client',
            name='lastName',
            field=models.CharField(max_length=60, verbose_name='lastName'),
        ),
    ]
