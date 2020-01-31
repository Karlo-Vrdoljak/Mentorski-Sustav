from django.urls import path, include
from mentorski.views import RegisterView
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('mentorski/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

]