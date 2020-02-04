from django.urls import path, include
from mentorski.views import RegisterView,courses,courseDetail
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('mentorski/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('courses/',courses,name='courses'),
    path('course/detail/<int:id>/',courseDetail, name="course details")
]