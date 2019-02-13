from django.urls import path
from . import views

urlpatterns = [
    path('', views.isi_blog, name='blog'),
    path('blog_list', views.blog_list, name='blog_list'),
    path('blog_looping', views.isi_blog, name='blog_looping'),
]