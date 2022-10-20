from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from main_app.models import Game, System

from .forms import PlayLog


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games})

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    play_log = PlayLog()
    systems_game_doesnt_have = System.objects.exclude(id__in = game.systems.all().values_list('id'))
    return render(request, 'games/detail.html', {
        'game': game,
        'play_log': play_log,
        'systems': systems_game_doesnt_have,
    })

def played_on(request, game_id):
    form = PlayLog(request.POST)
    if form.is_valid():
        new_log = form.save(commit=False)
        new_log.game_id = game_id
        new_log.save()
    return redirect('detail', game_id=game_id)

def assoc_system(request, game_id, system_id):
    Game.objects.get(id=game_id).systems.add(system_id)
    return redirect('detail', game_id=game_id)

class GameCreate(CreateView):
    model = Game
    fields = ['title', 'genre', 'description', 'esrb_rating']
    success_url = '/games/'

class GameUpdate(UpdateView):
    model = Game
    fields = ['genre', 'description', 'esrb_rating']
    success_url = '/games/'

class GameDelete(DeleteView):
    model = Game
    fields = '__all__'
    success_url = '/games/'

class SystemCreate(CreateView):
    model = System
    fields = ('name',)

class SystemUpdate(UpdateView):
    model = System
    fields = ('name',)

class SystemDelete(DeleteView):
    model = System
    success_url = '/systems/'

class SystemDetail(DetailView):
    model = System
    template_name = 'systems/detail.html'

class SystemList(ListView):
    model = System
    template_name = 'systems/index.html'



