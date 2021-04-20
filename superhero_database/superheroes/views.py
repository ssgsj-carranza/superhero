from django.shortcuts import render
from django.http import HttpResponse
from .models import Superheroes
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm


# Create your views here.

class SuperheroesForm(ModelForm):
    class Meta:
        model = Superheroes
        fields = ['heroes_name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catch_phrase']


def index(request):
    all_superheroes = Superheroes.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, "superheroes/index.html", context)


def detail(request, superhero_id):
    context = {"superheroes": Superheroes.objects.get(id=superhero_id)}
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/detail.html', context)
    # specific_superhero = Superheroes.objects.get(id=superhero_id)
    # context = {
    #     'specific_superhero': specific_superhero
    # }
    # return render(request, 'superheroes/detail.html', context)


def create(request):
    form = SuperheroesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    # if request.method == 'POST':
    #     heroes_name = request.POST.get('superhero name')
    #     alter_ego = request.POST.get('alter ego')
    #     primary_ability = request.POST.get('primary ability')
    #     secondary_ability = request.POST.get('secondary ability')
    #     catch_phrase = request.POST.get('catchphrase')
    #     new_superhero = Superheroes(heroes_name=heroes_name, alter_ego=alter_ego, primary_ability=primary_ability,
    #                                 secondary_ability=secondary_ability, catch_phrase=catch_phrase)
    #     new_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    context = {
        'form': form
    }

    return render(request, 'superheroes/create.html', context)


def delete(request, superhero_id):
    specific_superhero = Superheroes.objects.get(id=superhero_id)
    if request.method == 'POST':
        specific_superhero.delete()
        return HttpResponseRedirect(reverse('superheroes:index'))
    context = {
        'superheroes': specific_superhero
    }
    return render(request, 'superheroes/delete.html', context)


def update_hero(request, superhero_id):
    specific_superhero = Superheroes.objects.get(id=superhero_id)
    form = SuperheroesForm(request.POST or None, instance=specific_superhero)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    context = {
        'form': form
    }
    return render(request, 'superheroes/update_hero.html', context)
