from django.shortcuts import render
from django.http import HttpResponse
from .models import Superheroes


# Create your views here.


def index(request):
    all_superheroes = Superheroes.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, "superheroes/index.html")
