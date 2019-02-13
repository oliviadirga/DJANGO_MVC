from django.shortcuts import render

# Create your views here.
def daftar_mentor(request):
    return render(request, 'Mentor/mentor.html', {})