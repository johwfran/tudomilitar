# Generated by Django 3.1.7 on 2021-03-10 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='concurso',
            name='textantesdafoto',
            field=models.TextField(blank=True, help_text='TEXTO ANTES DA FOTO.', null=True, verbose_name='Texto1 do Concurso'),
        ),
        migrations.AddField(
            model_name='curiosidades',
            name='textantesdafoto',
            field=models.TextField(blank=True, help_text='TEXTO ANTES DA FOTO.', null=True, verbose_name='Texto1 da Curiosidade'),
        ),
    ]
