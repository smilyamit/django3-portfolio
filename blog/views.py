from django.shortcuts import render, get_object_or_404
from .models import Blogging

# Create your views here.
def allBlogs(request):
  # all_Blogs = Blogging.objects.all()
  all_Blogs = Blogging.objects.order_by('-date')     #for ordering date in reverse
  return render(request, 'blog/all_blogs.html', {'blogs':all_Blogs})

def details(request, blog_id):
  get_blog_id = get_object_or_404(Blogging, pk=blog_id)  #pk means primary key , its a keyword of db used in python
  return render(request, 'blog/detail.html', {'blog': get_blog_id})

# def allSports(request):
#   return render(request, 'blog/sports.html')