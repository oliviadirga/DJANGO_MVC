from django.shortcuts import render

# Create your views here.
def data_author(request):
    return render(request, 'Author/author.html', {})