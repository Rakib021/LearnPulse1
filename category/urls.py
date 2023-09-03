from django.urls import path
from . import views

urlpatterns = [
    path('courses/',views.single_course,name='single_course'),
    path('courses/<slug:slug>',views.course_detail,name="course_detail")
    
    
]

