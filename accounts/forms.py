from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Student

class SignUpForm(UserCreationForm):
    class Meta:
        fields = ("username","email","password1","password2")
        model = get_user_model()

class MaterialForm(forms.Form):
    title = forms.CharField()
    file  = forms.FileField()




