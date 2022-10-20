from django.db import models
from django.urls import reverse

# Create your models here.

class System(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('systems_index')

class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    description= models.TextField(max_length=250)
    esrb_rating = models.CharField(max_length=5)
    systems = models.ManyToManyField(System)

    def __str__(self):
        return self.title

class PlayedOn(models.Model):
    # .Field() creates a form to fill out
    date = models.DateField('Date Played')
    session_length = models.IntegerField(default=0)

    # Makes a foreign key
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.date