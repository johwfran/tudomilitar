from django.db import models

class Autor(models.Model):
    name = models.CharField(verbose_name="Nome do autor", max_length=60)
    city = models.CharField(verbose_name="Cidade do autor", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        
class Publicacoes(models.Model):
    title = models.CharField(verbose_name="Título da publicação", help_text="TÍTULO PRINCIPAL DA POSTAGEM.", max_length=150)
    author  = models.ForeignKey(Autor, verbose_name="Autor da publicação", on_delete=models.CASCADE)
    textantesdafoto  = models.TextField(verbose_name="Texto1 da publicação", help_text="TEXTO ANTES DA FOTO.", blank=True, null=True)
    image = models.ImageField(verbose_name="Imagem da publicação", upload_to="publicacoes")
    text  = models.TextField(verbose_name="Texto2 da publicação", help_text="TEXTO DEPOIS DA FOTO.")
    date   = models.DateField(verbose_name="Data da publicação", help_text="DATA DE LANÇAMENTO DA POSTAGEM.")
    category = models.CharField(verbose_name="Categoria da publicação", help_text="GERALMENTE É DO QUE SE TRATA A POSTAGEM.", max_length=100)
    Subject = models.CharField(verbose_name="Resumo da publicação", help_text="AQUI VOCÊ PODE COLOCAR UM BREVE RESUMO SOBRE O TEXTO EM SI.", max_length=150)
    change = models.DateField(verbose_name="Data de alteração da publicação", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Publicação"
        verbose_name_plural = "Publicações"

class Concurso(models.Model):
    title = models.CharField(verbose_name="Nome da Concurso", help_text="NOME DO CONCURSO.", max_length=150)
    author  = models.ForeignKey(Autor, verbose_name="Autor", on_delete=models.CASCADE)
    textantesdafoto  = models.TextField(verbose_name="Texto1 do Concurso", help_text="TEXTO ANTES DA FOTO.", blank=True, null=True)
    image = models.ImageField(verbose_name="Imagem da Concurso", upload_to="Concurso")
    text  = models.TextField(verbose_name="Sobre da Concurso", help_text="SOBRE DO CONCURSO.")
    date   = models.DateField(verbose_name="Data da Concurso")
    category = models.CharField(verbose_name="Categoria da Concurso", max_length=100)
    Subject = models.CharField(verbose_name="Resumo da Concurso", max_length=150)
    change = models.DateField(verbose_name="Data de alteração", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Concurso"
        verbose_name_plural = "Concursos"


class Curiosidades(models.Model):
    title = models.CharField(verbose_name="Nome da Curiosidade", help_text="Nome Da Curiosidade.", max_length=150)
    author  = models.ForeignKey(Autor, verbose_name="Autor", on_delete=models.CASCADE)
    textantesdafoto  = models.TextField(verbose_name="Texto1 da Curiosidade", help_text="TEXTO ANTES DA FOTO.", blank=True, null=True)
    image = models.ImageField(verbose_name="Imagem da Curiosidade", upload_to="Curiosidade")
    text  = models.TextField(verbose_name="Sobre da Curiosidade", help_text="Sobre a Curiosidade.")
    date   = models.DateField(verbose_name="Data da Curiosidade")
    category = models.CharField(verbose_name="Categoria da Curiosidade", max_length=100)
    Subject = models.CharField(verbose_name="Resumo da Curiosidade", max_length=150)
    change = models.DateField(verbose_name="Data de alteração", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Curiosidade"
        verbose_name_plural = "Curiosidades"
        