from django.urls import path
from . import views

urlpatterns = [
    path('', views.isi_blog, name='blog'),
]