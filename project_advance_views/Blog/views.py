from django.shortcuts import render, redirect
from .models import Blog
from .forms import Form

# Create your views here.
def isi_blog(request):
    blogspot = Blog.objects.all()
    return render(request, 'Blog/blog_looping.html', { 'blogs': blogspot})

def blog_list(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save
            form.save()
            return redirect('blog')

    else:
        form = Form()
    return render(request, 'Blog/blog_form.html', {'form': form})
