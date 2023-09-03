from django.contrib import admin
from category.models import Course
# Register your models here.



class CourseStoreModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'department', 'price','status','featured_video')

admin.site.register(Course, CourseStoreModelAdmin)