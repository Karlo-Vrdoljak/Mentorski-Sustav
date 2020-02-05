from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView
from mentorski.users.forms import CustomUserCreationForm
from mentorski.models import Predmeti
from django.http import HttpResponse
from django.shortcuts import render, redirect
from mentorski.forms import PredmetCreate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

# GET mapping
@login_required
def courses(request):
    all_courses = Predmeti.objects.all()
    courses = []
    for course in all_courses:
        if len(course.program.split(' ')) > 4:
            course.program = (' '.join(course.program.split(' ')[:4]) + ' ...')
        courses.append(course)

    return render(request, 'courses.html', {'courses':courses})


@login_required
@require_http_methods(["GET","POST"])
def courseDetail(request,id):
    pkPredmet = int(id)
    if request.method == 'GET':
        try:
            predmet = Predmeti.objects.get(id = pkPredmet)
        except Predmeti.DoesNotExist:
            return redirect('courses')
        predmetForm = PredmetCreate(instance=predmet)
        return render(request,'courseDetail.html', {'predmetForm':predmetForm, 'predmet_ime': predmet.kod})
    elif request.method == 'POST':
        db_model = Predmeti.objects.get(id = int(id))
        form = PredmetCreate(request.POST,instance=db_model)
       
        if form.is_valid():
            # db_model.ime = form.cleaned_data['ime']
            # db_model.save()
            form.save()
            return redirect('courses')
        else:
            return render(request,'courses.html', {'predmetForm':form, 'predmet_ime': db_model.kod})
    

@login_required
@require_http_methods(["GET"])
def courseDelete(request,id):
    pkPredmet = int(id)
    if request.method == 'GET':
        Predmeti.objects.get(id = pkPredmet).delete()
        return redirect('courses')


@login_required
@require_http_methods(["GET","POST"])
def new_course(request):
    if request.method == 'GET':
        predmetForm = PredmetCreate()
        return render(request,'courseNew.html', {'predmetForm':predmetForm, 'course_title': 'New course'})
    elif request.method == 'POST':
        db_model = Predmeti()
        form = PredmetCreate(request.POST,instance=db_model)

        if form.is_valid():
            form.save()
            return redirect('courses')
        else:
            predmetForm = PredmetCreate()
            return render(request,'courseNew.html', {'predmetForm':predmetForm, 'course_title': 'New course'})
        

