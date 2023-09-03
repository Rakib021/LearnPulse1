from django.shortcuts import render, redirect
from category.models import Course
from .forms import CourseStoreForm

def add_courses(request):
        if request.method == 'POST':
            course = CourseStoreForm(request.POST,request.FILES)
            if course.is_valid():
               course.save(commit=True)
               print('hello',course)
               return redirect('showcourse')

        else:
              course = CourseStoreForm()
              
        return render(request, 'add_course.html', {'form':course})

def show_course(request):
     course = Course.objects.all()
     return render(request, 'show_course.html', {'data': course})

def edit(request,id):
      course = Course.objects.get(pk=id)
      form = CourseStoreForm(instance=course)
      if request.method =='POST':
            form = CourseStoreForm(request.POST,instance=course)
            
            if form.is_valid():
               form.save()
               return redirect('showcourse')
               
            
      return render(request, 'add_course.html', {'form':form})

def delete_course(request,id):
      course = Course.objects.get(pk=id).delete()
      return redirect('showcourse')
      