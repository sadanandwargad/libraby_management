from django.urls import path
from django.http import HttpResponse
from .import views


urlpatterns = [
     path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),

    path('register/',views.registerPage, name="register"),

    path('',views.home,name='home'),

    path('create-book/',views.createBook, name="create-book"),
    path('update-book/<str:pk>',views.updateBook,name="update-book"),
    #delete book
    path('delete-book/<str:pk>',views.deleteBook,name="delete-book"),
    #view book details
    path('view-book/<str:pk>',views.viewBook,name="view-book"),



]