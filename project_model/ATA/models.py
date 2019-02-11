from django.db.models import TextField
from django.db.models import CharField
from django.db import models
from django.utils import timezone

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.TextField(max_length=255)
    no_telepon = models.CharField(max_length=25)
    jabatan = models.TextField(max_length=50)

class Mantee(models.Model):
    nama_lengkap = models.TextField(max_length=255)
    no_telepon = models.CharField(max_length=25)
    no_absen = models.CharField(max_length=5)
    nilai_rata_rata = models.CharField(max_length=5)
    
class MataPelajaran(models.Model):
    nama_pelajaran = models.TextField(max_length=255)
    jadwal_dimulai = models.DateTimeField(default=timezone.now)
    jadwal_berakhir = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nama_pelajaran

class Mentor(models.Model):
    nama_lengkap = models.TextField(max_length=255)
    no_telepon = models.CharField(max_length=25)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

class Challenge(models.Model):
    nama_challenge = models.TextField(max_length=255)
    banyak_soal = models.CharField(max_length=3)
    bobot_nilai = models.CharField(max_length=3)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

class LiveCode(models.Model):
    nama_live_code = models.TextField(max_length=255)
    banyak_soal = models.CharField(max_length=3)
    bobot_nilai = models.CharField(max_length=3)
    tanggal_pelaksanaan = models.DateTimeField(default=timezone.now)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

