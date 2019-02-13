from django.urls import path
from . import views

urlpatterns = [
    path('', views.isi_home, name='home'),
]