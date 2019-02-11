from django.contrib import admin

# Register your models here.
from .models import Direksi, Mantee, Mentor, MataPelajaran, Challenge, LiveCode

my_model = [Direksi, Mantee, Mentor, MataPelajaran, Challenge, LiveCode]
admin.site.register(my_model)