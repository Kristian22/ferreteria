# Generated by Django 4.2.4 on 2023-08-24 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crud',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=15)),
                ('creditos', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
