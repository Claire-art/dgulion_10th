from django.shortcuts import redirect, render,get_object_or_404
from .models import Post
from django.utils import timezone


def showmain(request):
    posts = Post.objects.all()
    return render(request , 'main/mainpage.html' , {'posts':posts})

def detail(request,id):
    post = get_object_or_404(Post, pk = id)
    return render(request , 'main/detail.html',{'post':post})

def new(request):
    return render(request , 'main/new.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_data = timezone.now()
    new_post.body = request.POST['body']
    new_post.save()
    return redirect('detail' , new_post.id)