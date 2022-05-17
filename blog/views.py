# 16e---personal_portfolio_project/blog/views.py, add: , get_object_or_404
from django.shortcuts import render, get_object_or_404

# 14a---in personal_portfolio_project/blog/views.py, add:
from .models import Blog


# Create your views here.

# 11d---in personal_portfolio_project/blog/views.py, add:
def all_blogs(request):

    # 14b---in personal_portfolio_project/blog/views.py, def all_blogs(request):, add: blogs = Blog.objects.all()
    # blogs = Blog.objects.all()
    # or
    blogs = Blog.objects.order_by('-date')
    # or
    # blogs = Blog.objects.order_by('-date')[:5]

    # 14c---in personal_portfolio_project/blog/views.py, def all_blogs(request):, add: , {'blogs':blogs}
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})


# 16b---personal_portfolio_project/blog/views.py, add:
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)  # 16f---personal_portfolio_project/blog/views.py, add: blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
