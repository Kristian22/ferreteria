# Generated by Django 4.2.4 on 2023-11-24 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crud', '0002_sistemaviajes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('codigo_manager', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('correo', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='sistemaviajes',
            name='num_telefono',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='sistemaviajes',
            name='turno',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
