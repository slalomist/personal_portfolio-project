from django.shortcuts import render, get_object_or_404

from .models import Blog


def all_blocks(request):
    blogs = Blog.objects.order_by('-data')
    return render(request, 'blog/all_blocks.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
