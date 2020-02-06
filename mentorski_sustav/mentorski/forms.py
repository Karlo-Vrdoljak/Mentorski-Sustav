from django import forms
from mentorski.models import Predmeti, CustomUser

class PredmetCreate(forms.ModelForm):
    class Meta:
        model = Predmeti
        fields = '__all__'

class Student(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'