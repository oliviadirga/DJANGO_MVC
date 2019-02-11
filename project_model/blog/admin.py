from django.contrib import admin

# Register your models here.
from .models import BlogPost, Mantee

my_model = [BlogPost, Mantee]
admin.site.register(my_model)