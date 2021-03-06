from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
#The dot before models means current directory or current application. Both views.py and models.py are in the same directory.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html',{'posts':posts})

#request (everything we receive from the user via the Internet)
#Template file ('blog/post_list.html').

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})