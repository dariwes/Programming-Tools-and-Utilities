from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile


class UserCreationFormProfile(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = UserCreationForm.Meta.fields


class UserChangeFormProfile(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = UserChangeForm.Meta.fields
