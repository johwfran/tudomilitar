from django.contrib import admin
from .models import Autor, Publicacoes, Concurso, Curiosidades

admin.site.register(Autor)
admin.site.register(Publicacoes)
admin.site.register(Concurso)
admin.site.register(Curiosidades)
