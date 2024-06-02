from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-date')
    message = "no hay post aun"
    return render(request, 'post/post_list.html', {"posts":posts, "message":message})


def  post_page(request, slug):
     return HttpResponse(slug)