# Generated by Django 5.1.6 on 2025-03-07 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_piloto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piloto',
            name='fecha_creacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
