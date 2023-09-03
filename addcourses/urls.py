from django.urls import path,include

from . import views



urlpatterns = [
   path('add_course/', views.add_courses, name='addcourse'),
   path('show_course/', views.show_course, name='showcourse'),
   path('edit_course/<int:id>', views.edit, name='editcourse'),
   path('delete_course/<int:id>', views.delete_course, name='deletecourse'),

    

] 
