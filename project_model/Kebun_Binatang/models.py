from django.db.models import TextField
from django.db.models import CharField
from django.db import models
from django.utils import timezone
# Create your models here.
class Hewan(models.Model):
    nama = models.TextField(max_length=255)
    species = models.TextField(max_length=50)
    berat = models.CharField(max_length=3)
    umur = models.CharField(max_length=3)

class Kandang(models.Model):
    nama = models.TextField(max_length=255)
    isi_kandang = models.TextField(max_length=255)
    luas_kandang = models.CharField(max_length=5)

class Penjaga(models.Model):
    nama = models.TextField(max_length=255)
    nomor_telepon = models.CharField(max_length=25)
    jadwal_jaga = models.DateTimeField(default=timezone.now)

class Pengunjung(models.Model):
    nama = models.TextField(max_length=255)
    nomor_telepon = models.CharField(max_length=25)
    hari_berkunjung = models.TextField(max_length=10)