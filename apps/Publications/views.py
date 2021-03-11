from django.shortcuts import render
from .models import Concurso
from .models import Publicacoes
from .models import Curiosidades

def concurso(request):
    Publication = Concurso.objects.all()
    return render(request, 'publications/concurso.html',locals())

def index(request):
    Publication = Publicacoes.objects.all()
    return render(request, 'publications/index.html',locals())

def curiosidades(request):
    Publication = Curiosidades.objects.all()
    return render(request, 'publications/curiosidades.html',locals())

def quemsomos(request):
    return render(request, 'publications/quemsomos.html',locals())

def recomendamos(request):
    return render(request, 'publications/recomendamos.html',locals())
