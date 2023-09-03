from django.shortcuts import render ,redirect
from category.models import Categories,Course


def base(request):
    return render(request,'base.html')
def home(request):
    category =Categories.objects.all().order_by('id')[0:5]
    course =Course.objects.filter(status='PUBLISH').order_by('-id')
    
    context ={
        'category':category,
        'course':course,
    }
    return render(request,'main/home.html',context)

def about(request):
    return render (request,'contents/about.html')


