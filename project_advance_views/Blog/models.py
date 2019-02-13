from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    judul = models.CharField(max_length=200, default='')
    deskripsi = models.CharField(max_length=200, default='')
    images = models.ImageField(upload_to='Media/img')
    komentar = models.CharField(max_length=200, default='')
    waktu_update = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.judul
