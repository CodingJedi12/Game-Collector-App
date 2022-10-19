from telnetlib import GA
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PlayLog

from main_app.models import Game

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
    return render(request, 'games/detail.html', {
        'game': game,
        'play_log': play_log
    })

def played_on(request, game_id):
    form = PlayLog(request.POST)
    if form.is_valid():
        new_log = form.save(commit=False)
        new_log.game_id = game_id
        new_log.save()
    return redirect('detail', game_id=game_id)

class GameCreate(CreateView):
    model = Game
    fields = '__all__'
    success_url = '/games/'

class GameUpdate(UpdateView):
    model = Game
    fields = ['genre', 'description', 'esrb_rating']
    success_url = '/games/'

class GameDelete(DeleteView):
    model = Game
    fields = '__all__'
    success_url = '/games/'
