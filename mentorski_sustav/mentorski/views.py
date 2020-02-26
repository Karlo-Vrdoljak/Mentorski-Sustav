from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView,DetailView
from mentorski.users.forms import CustomUserCreationForm, CustomUserChangeForm
from mentorski.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from mentorski.forms import PredmetCreate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from mentorski_sustav.settings import IZVANREDNI_SEM, REDOVNI_SEM
from mentorski.mentorskiService import MentorskiService
from django.http import HttpResponseRedirect

mentorskiService = MentorskiService()
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


@login_required
def reroute(request):
    if request.user.role == 'mentor': 
        return HttpResponseRedirect(reverse('courses', args=[]))
    else:
        return HttpResponseRedirect(reverse('upisni list', args=[request.user.id]))

@login_required
def courses(request):
    all_courses = Predmeti.objects.all()
    courses = mentorskiService.getAllSubjects()
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
@require_http_methods(["POST"])
def courseDelete(request,id):
    pkPredmet = int(id)
    if request.method == 'POST':
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
        

@login_required
@require_http_methods(["GET"])
def students(request):
    if request.method == 'GET':
        users = CustomUser.objects.all()
        students = [user for user in users if user.role == 'student']
        return render(request, 'students.html', {'students':students, 'students_title':'All students'})

@login_required
@require_http_methods(["GET", "POST"])
def student_details(request,id):
    if request.method == 'GET':
        try:
            user = CustomUser.objects.get(id = int(id))
        except CustomUser.DoesNotExist:
            return redirect('students')
        studentForm = CustomUserChangeForm(instance=user)
        return render(request,'studentDetail.html', {'studentForm':studentForm, 'student_ime': user.email})

    elif request.method == 'POST':
        db_model = CustomUser.objects.get(id = int(id))
        form = CustomUserChangeForm(request.POST,instance=db_model)
       
        if form.is_valid():
            form.save()
            return redirect('students')
        else:
            return render(request,'studentDetail.html', {'studentForm':studentForm, 'student_ime': user.email})



@login_required
@require_http_methods(["POST"])
def student_delete(request,id):
    if request.method == 'POST':
        CustomUser.objects.get(id = int(id)).delete()
        return redirect('students')




@login_required
@require_http_methods(["GET","POST"])
def student_upisni_list(request,id):
    if request.method == 'GET':
        courses = mentorskiService.getAllSubjects()
        student = CustomUser.objects.get(id = int(id))
        upis__student, upis__predmet = mentorskiService.getUpisiPredmeti__Studenti()
        subject_semester = mentorskiService.groupPredmeti(upis__predmet,student)

        upisi_student = mentorskiService.getUpisiStudent()

        filteredCourses = [] 
        for item in courses:
            if item not in upisi_student:
                filteredCourses.append(item) 
        courses = filteredCourses

        return render(request, 'upisniList.html', 
        {
            'courses':courses, 
            'student':student,
            'upis__student':upis__student,
            'upis__predmet': upis__predmet,
            'subject_semester':subject_semester
        })
    elif request.method == 'POST':
        selected_predmet = Predmeti.objects.get(id=int(id))
        upisi_model = Upisi()
        upisi_model.student = CustomUser.objects.get(id=int(mentorskiService.getStudentId()))
        upisi_model.predmet = Predmeti.objects.get(id = int(id))
        upisi_model.status = 'enrolled'

        upisi_model.save()
        return HttpResponseRedirect(reverse('upisni list', args=[int(mentorskiService.getStudentId())]))


@login_required
@require_http_methods(["POST"])
def student_upisni_list_remove(request,id):
    if request.method == 'POST':
        course = Predmeti.objects.get(id = int(id))
        upisi_student = mentorskiService.getUpisi()
        for item in upisi_student:
            if item.predmet.id == id:
                upis = Upisi.objects.get(id=int(item.id)).delete()
                break
        return HttpResponseRedirect(reverse('upisni list', args=[int(mentorskiService.getStudentId())]))
        
@login_required
@require_http_methods(["POST"])
def student_upisni_list_pass(request,id):
    if request.method == 'POST':
        course = Predmeti.objects.get(id = int(id))
        upisi_student = mentorskiService.getUpisi()
        for item in upisi_student:
            if item.predmet.id == id:
                upis = Upisi.objects.get(id=int(item.id))
                upis.status = 'passed'
                upis.save()
                break
        return HttpResponseRedirect(reverse('upisni list', args=[int(mentorskiService.getStudentId())]))

@login_required
@require_http_methods(["GET"])     
def report(request):
    courses = mentorskiService.getAllSubjectsHigherThanEcts(6)
    if len(courses) > 0:
        return render(request, 'reportEcts.html', { 'courses':courses })

