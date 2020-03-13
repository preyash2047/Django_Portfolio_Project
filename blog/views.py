from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.http import HttpResponse

# Create your views here.
def allblogs(request):
    Blogs = Blog.objects
    return render(request, "blog/allblogs.html", {'Blogs':Blogs})

def detail(request, blog_id):
    detailBlog = get_object_or_404(Blog, pk=blog_id)
    #return HttpResponse(detailBlog.title)
    return render(request, 'blog/detail.html', {'detailBlog':detailBlog})
