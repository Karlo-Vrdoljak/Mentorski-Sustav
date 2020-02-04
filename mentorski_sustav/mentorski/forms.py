from django import forms
from mentorski.models import Predmeti

class PredmetCreate(forms.ModelForm):
    class Meta:
        model = Predmeti
        fields = '__all__'