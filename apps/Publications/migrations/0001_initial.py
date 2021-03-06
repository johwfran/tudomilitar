# Generated by Django 3.1.7 on 2021-03-10 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Nome do autor')),
                ('city', models.CharField(max_length=30, verbose_name='Cidade do autor')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Publicacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='TÍTULO PRINCIPAL DA POSTAGEM.', max_length=150, verbose_name='Título da publicação')),
                ('textantesdafoto', models.TextField(help_text='TEXTO ANTES DA FOTO.', verbose_name='Texto1 da publicação')),
                ('image', models.ImageField(blank=True, null=True, upload_to='publicacoes', verbose_name='Imagem da publicação')),
                ('text', models.TextField(blank=True, help_text='TEXTO DEPOIS DA FOTO.', null=True, verbose_name='Texto2 da publicação')),
                ('date', models.DateField(help_text='DATA DE LANÇAMENTO DA POSTAGEM.', verbose_name='Data da publicação')),
                ('category', models.CharField(help_text='GERALMENTE É DO QUE SE TRATA A POSTAGEM.', max_length=100, verbose_name='Categoria da publicação')),
                ('Subject', models.CharField(help_text='AQUI VOCÊ PODE COLOCAR UM BREVE RESUMO SOBRE O TEXTO EM SI.', max_length=150, verbose_name='Resumo da publicação')),
                ('change', models.DateField(blank=True, null=True, verbose_name='Data de alteração da publicação')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Publications.autor', verbose_name='Autor da publicação')),
            ],
            options={
                'verbose_name': 'Publicação',
                'verbose_name_plural': 'Publicações',
            },
        ),
        migrations.CreateModel(
            name='Curiosidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Nome Da Curiosidade.', max_length=150, verbose_name='Nome da Curiosidade')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Curiosidade', verbose_name='Imagem da Curiosidade')),
                ('text', models.TextField(help_text='Sobre a Curiosidade.', verbose_name='Sobre da Curiosidade')),
                ('date', models.DateField(verbose_name='Data da Curiosidade')),
                ('category', models.CharField(max_length=100, verbose_name='Categoria da Curiosidade')),
                ('Subject', models.CharField(max_length=150, verbose_name='Resumo da Curiosidade')),
                ('change', models.DateField(blank=True, null=True, verbose_name='Data de alteração')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Publications.autor', verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Curiosidade',
                'verbose_name_plural': 'Curiosidades',
            },
        ),
        migrations.CreateModel(
            name='Concurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='NOME DO CONCURSO.', max_length=150, verbose_name='Nome da Concurso')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Concurso', verbose_name='Imagem da Concurso')),
                ('text', models.TextField(help_text='SOBRE DO CONCURSO.', verbose_name='Sobre da Concurso')),
                ('date', models.DateField(verbose_name='Data da Concurso')),
                ('category', models.CharField(max_length=100, verbose_name='Categoria da Concurso')),
                ('Subject', models.CharField(max_length=150, verbose_name='Resumo da Concurso')),
                ('change', models.DateField(blank=True, null=True, verbose_name='Data de alteração')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Publications.autor', verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Concurso',
                'verbose_name_plural': 'Concursos',
            },
        ),
    ]
