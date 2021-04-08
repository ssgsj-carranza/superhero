from django.shortcuts import render
from django.http import HttpResponse
from .models import Superheroes
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def index(request):
    all_superheroes = Superheroes.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, "superheroes/index.html", context)


def detail(request, superheroes_id):
    all_superheroes = Superheroes.objects.all()
    context = {
        'all_superheroes': Superheroes.objects.filter()
    }
    return render(request, str(superheroes_id), "superheroes/index.html", context)


def create(request):
    if request.method == 'POST':
        superhero_name = request.POST.get('superhero name')
        alter_ego = request.POST.get('alter ego')
        primary_ability = request.POST.get('primary ability')
        secondary_ability = request.POST.get('secondary ability')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = Superheroes(superhero_name=superhero_name, alter_ego=alter_ego, primary_ability=primary_ability,
                                    secondary_ability=secondary_ability, catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')


def delete(conn, id):
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()