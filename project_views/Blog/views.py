from django.shortcuts import render

# Create your views here.
def isi_blog(request):
    return render(request, 'Blog/blog.html', {})