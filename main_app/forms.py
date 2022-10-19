from django.forms import ModelForm
from .models import PlayedOn

class PlayLog(ModelForm):
    class Meta:
        model = PlayedOn
        fields = ['date']