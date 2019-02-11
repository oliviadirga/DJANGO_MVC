from django.contrib import admin

# Register your models here.
from .models import Dokter, Pasien, Resep, Obat

my_model = [Dokter, Pasien, Resep, Obat]
admin.site.register(my_model)