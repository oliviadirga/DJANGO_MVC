from django.contrib import admin

# Register your models here.
from .models import Hewan, Kandang, Penjaga, Pengunjung

my_model = [Hewan, Kandang, Penjaga, Pengunjung]
admin.site.register(my_model)