from django.shortcuts import render
from .models import Categories,Course
from django.http import Http404


# Create your views here.
def single_course(request):
    category = Categories.get_all_categories(Categories)
    
    course =Course.objects.filter(status='PUBLISH').order_by('-id')

    
    context ={
        'category' :category,
        'course':course,
    }
    

    return render(request,'course/single_course.html',context)

def course_detail(request, slug):
    category = Categories.get_all_categories(Categories)
    try:
        course = Course.objects.get(slug=slug)
    except Course.DoesNotExist:
        raise Http404("Course does not exist")

    context = {
        'course': course,
        'category': category
    }
    return render(request, 'course/course_detail.html', context)