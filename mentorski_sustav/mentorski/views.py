from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from mentorski.users.forms import CustomUserCreationForm
from mentorski.models import Predmeti
from django.http import HttpResponse
from django.shortcuts import render, redirect

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

def courses(request):
    all_courses = Predmeti.objects.all()
    return render(request, 'courses.html', {'courses':all_courses})
