from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    description= models.TextField(max_length=250)
    esrb_rating = models.CharField(max_length=5)

    def __str__(self):
        return self.title