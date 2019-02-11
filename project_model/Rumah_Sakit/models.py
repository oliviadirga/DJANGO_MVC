from django.db.models import TextField
from django.db import models
from django.utils import timezone

# Create your models here.
class Dokter(models.Model):
    nama = models.TextField(max_length=255)
    nomor_telepon = models.CharField(max_length=25)
    bidang = models.TextField(max_length=50)
    jadwal_praktek = models.DateTimeField(default=timezone.now)

class Pasien(models.Model):
    nama = models.TextField(max_length=255)
    nomor_telepon = models.CharField(max_length=25)
    alamat = models.CharField(max_length=255)
    keluhan = models.TextField(max_length=255)

class Resep(models.Model):
    nama = models.TextField(max_length=255)
    total_harga = models.CharField(max_length=25)
    kumpulan_obat = models.TextField(max_length=255)

class Obat(models.Model):
    nama = models.TextField(max_length=255)
    kandungan = models.TextField(max_length=255)
    khasiat = models.TextField(max_length=255)