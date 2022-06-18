from email import message
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .models import Book,User
from .forms import UserForm ,BookForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required



# Create your views here.

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'email or password does not exist')
    context = {'page':page}
    return render(request,'base/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'An error Occured')

    return render(request,'base/login_register.html',{'form':form})



def home(request):
    
    books = Book.objects.all()
    book_count = books.count()
    context = {'books':books,'book_count':book_count}

    return render(request,'base/home.html',context)

@login_required(login_url='login')
def createBook(request):
    form  = BookForm()         
    
    if request.method =='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.admin =request.user
            print(obj.admin)
            obj.save()
            messages.success(request,'New book record is created!')
            return redirect('home')

    context = {'form':form}
    return render(request,'base/book_form.html',context)

def updateBook(request,pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book) 
    if request.user != book.admin:
        return HttpResponse('Your not allowed here!!' )

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request,'base/book_form.html',context)

def deleteBook(request,pk):
    book = Book.objects.get(id=pk)
    if request.user != book.admin:
        return HttpResponse('Your not allowed here!!' )
    else:
        book.delete()
        messages.success(request, 'The book '+ book.name + ' was deleted successfully.')
        return redirect('home')

def viewBook(request,pk):
    book = Book.objects.get(id=pk)
    context = {"book": book}
    return render(request,'base/view_book.html',context)