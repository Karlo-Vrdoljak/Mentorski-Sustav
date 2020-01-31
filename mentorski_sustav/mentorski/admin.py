from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from mentorski.users.forms import CustomUserCreationForm, CustomUserChangeForm
from mentorski.models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username','role', 'status']

admin.site.register(CustomUser, CustomUserAdmin)