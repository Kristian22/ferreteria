# Generated by Django 4.2.4 on 2023-11-14 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SistemaViajes',
            fields=[
                ('num_viaje', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('articulos', models.CharField(max_length=70)),
                ('hora_entrega_estimado', models.CharField(max_length=5)),
                ('turno', models.PositiveSmallIntegerField(max_length=2)),
                ('direccion', models.CharField(max_length=70)),
                ('num_telefono', models.PositiveSmallIntegerField(max_length=10)),
            ],
        ),
    ]
