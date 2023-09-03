from django import forms
from category.models import Course



class CourseStoreForm(forms.ModelForm):
    class Meta:
        model = Course
        
        fields = "__all__"
        exclude =['slug']
        

        