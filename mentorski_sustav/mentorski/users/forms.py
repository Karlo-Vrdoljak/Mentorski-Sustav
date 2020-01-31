from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from mentorski.models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role', 'status')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role', 'status')