from django.shortcuts import render

# Create your views here.
def daftar_mentee(request):
    return render(request, 'Mentee/mentee.html', {})