# Generated by Django 5.1.6 on 2025-02-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_curso_professor'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='duracao',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
