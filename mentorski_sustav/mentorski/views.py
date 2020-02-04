from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from mentorski.users.forms import CustomUserCreationForm
from mentorski.models import Predmeti
from django.http import HttpResponse
from django.shortcuts import render, redirect
from mentorski.forms import PredmetCreate
from django.contrib.auth.decorators import login_required

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

# GET mapping
@login_required
def courses(request):
    all_courses = Predmeti.objects.all()
    return render(request, 'courses.html', {'courses':all_courses})

# GET mapping
@login_required
def courseDetail(request,id):
    pkPredmet = int(id)
    try:
        predmet = Predmeti.objects.get(id = pkPredmet)
    except Predmeti.DoesNotExist:
        return redirect('courses')
    predmetForm = PredmetCreate(instance=predmet)
    return render(request,'courseDetail.html', {'predmetForm':predmetForm, 'predmet_ime': predmet.kod})