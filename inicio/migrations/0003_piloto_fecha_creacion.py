# Generated by Django 5.1.6 on 2025-03-06 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_alter_piloto_puntos'),
    ]

    operations = [
        migrations.AddField(
            model_name='piloto',
            name='fecha_creacion',
            field=models.DateField(null=True),
        ),
    ]
