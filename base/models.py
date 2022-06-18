from pydoc import describe
from pyexpat import model
from turtle import update
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager     ## A new class is imported. ##
from django.utils.translation import ugettext_lazy as _

#Create a custom Manager for the new User model


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

#-------------------------------------------------------------------------------------------


# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique = True,null = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Book(models.Model):
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField(null=True,blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.name