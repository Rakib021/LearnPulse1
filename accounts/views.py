from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from category.models import Course
from django.contrib import messages
from django.http import HttpResponse 



def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')


        if User.objects.filter(email=email).exists():
           messages.warning(request,'Email are Already Exists !')
           return redirect('register')


        if User.objects.filter(username=username).exists():
           messages.warning(request,'Username are Already exists !')
           return redirect('register')

        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return redirect('login')

    return render(request,'registration/register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
		
        user = authenticate(request, username=username, password=password)

        if user is not None:
           login(request, user)
           return redirect('home')
        else:
           messages.error(request, 'Username and Password Are Invalid !')


    return render(request, 'registration/login.html') 
		   
     
def profile(request):
    return render(request,'registration/profile.html')

def profile_update(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id
        print('hello' ,user_id)

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request,'Profile Are Successfully Updated. ')
        return redirect('profile')
    
def search(request):
    query = request.GET['query']
    course = Course.objects.filter(title__icontains = query)
    
    context ={
        'course':course
    }
    
    return render(request,'registration/search.html',context)