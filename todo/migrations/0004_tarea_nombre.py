# Generated by Django 4.1.1 on 2022-10-13 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_tarea_nombre_tarea_lugar'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='nombre',
            field=models.CharField(default=2, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]