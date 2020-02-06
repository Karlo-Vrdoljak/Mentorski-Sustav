from django.urls import path, include
from mentorski.views import *
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('mentorski/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('reroute/', reroute, name='reroute'),
    path('courses/',courses,name='courses'),
    path('course/new/',new_course, name="new course"),
    path('course/detail/<int:id>/',courseDetail, name="course details"),
    path('course/delete/<int:id>/',courseDelete, name="course delete"),
    path('students/',students, name="students"),
    path('student/detail/<int:id>/',student_details, name="student details"),
    path('student/delete/<int:id>/',student_delete, name="student delete"),
    path('upisni-list/<int:id>/',student_upisni_list, name="upisni list"),
    path('upisni-list/remove/<int:id>/',student_upisni_list_remove, name="upisni list remove"),
    path('upisni-list/pass/<int:id>/',student_upisni_list_pass, name="upisni list pass"),

]