from django.forms import  ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CategoryForm(forms.ModelForm):
    class Meta: 
        model = Category
        fields ="__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"