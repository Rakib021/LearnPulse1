from django.contrib import admin

# Register your models here.
from .models import Categories,Author

admin.site.register(Categories)
admin.site.register(Author)
