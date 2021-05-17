from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from .forms import UserCreationFormProfile, UserChangeFormProfile


class UserAdminProfile(UserAdmin):
    add_form = UserCreationFormProfile
    form = UserChangeFormProfile
    list_display = ['email', 'username', 'age']
    model = UserProfile


admin.site.register(UserProfile, UserAdminProfile)
