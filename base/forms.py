from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import Book,User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','password1','password2']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name','author','content']
        