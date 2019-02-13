from django.shortcuts import render

# Create your views here.
def isi_home(request):
    return render(request, 'Home/home.html', {})