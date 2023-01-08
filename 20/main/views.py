from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog , Comment,Like, Dislike
from django.utils import timezone
from django.db import models
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json
from django.contrib.auth.models import User


# mainpage view 함수
def main(request):
    return render(request, 'main/mainpage.html')

def posts(request):
    blogs = Blog.objects.all()
    return render(request, 'main/posts.html', {'blogs':blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    all_comments = blog.comments.all().order_by('-created_at')
    return render(request, 'main/detail.html', {'blog':blog, 'comments':all_comments})


def new(request):
    return render(request, 'main/new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.user
    new_blog.pub_date = timezone.now()
    new_blog.body = request.POST['body']
    new_blog.image = request.FILES.get('image')
    new_blog.save()
    return redirect('main:detail', new_blog.id)

def edit(request , id):
    edit_blog = Blog.objects.get(id=id)
    return render(request , 'main/edit.html' , {'blog':edit_blog})

def update(request , id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.user
    update_blog.pub_date = timezone.now()
    update_blog.body = request.POST['body']
    update_blog.image = request.FILES.get('image')
    update_blog.save()
    return redirect('main:detail', update_blog.id)    

def delete(request , id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('main:posts')


def create_comment(request, blog_id):
    new_comment = Comment()
    new_comment.writer = request.user
    new_comment.content = request.POST['content']
    new_comment.blog = get_object_or_404(Blog, pk = blog_id)
    new_comment.save() 
    return redirect('main:detail', blog_id)

def delete_comment(request,id):
    comment = get_object_or_404(Comment, pk=id)
    post_id = comment.blog.id
    comment.delete()
    return redirect('main:detail', post_id)

def edit_comment(request, id):
    edit_comment = Comment.objects.get(id = id)
    return render(request, 'main/edit_comment.html', {'comment' : edit_comment})

def update_comment(request, id):
    print("update Comment content = " + request.POST['content'])
    update_comment = Comment.objects.get(id = id)
    update_comment.content = request.POST['content']
    update_comment.update_at = models.DateTimeField(auto_now=True)
    update_comment.save()
    return redirect('main:detail', update_comment.blog.id)


@require_POST
@login_required
def like_toggle(request, post_id):
    post = get_object_or_404(Blog, pk = post_id)
    post_like, post_like_created = Like.objects.get_or_create(user = request.user, post=post)

    if not post_like_created:
        post_like.delete()
        result = "cancelled"

    else:
        result = "like"
    
    context = {
        "like_count" : post.like_count,
        "result" : result
    }

    return HttpResponse(json.dumps(context), content_type = "application/json")

@require_POST
@login_required
def like_toggle(request, post_id):
    post = get_object_or_404(Blog, pk = post_id)
    post_like, post_like_created = Like.objects.get_or_create(user = request.user, post=post)

    if not post_like_created:
        post_like.delete()
        result = "cancelled"

    else:
        result = "like"
    
    context = {
        "like_count" : post.like_count,
        "result" : result
    }

    return HttpResponse(json.dumps(context), content_type = "application/json")

def my_like(request, user_id):
    user = User.objects.get(id=user_id)
    like_list = Like.objects.filter(user = user)
    context = {
        'like_list' : like_list,
    } 

    return render(request, 'main/my_like.html', context)

@require_POST
@login_required
def dislike_toggle(request, post_id):
    post = get_object_or_404(Blog, pk = post_id)
    post_dislike, post_dislike_created = Dislike.objects.get_or_create(user = request.user, post=post)

    if not post_dislike_created:
        post_dislike.delete()
        result = "cancelled"

    else:
        result = "dislike"
    
    context = {
        "dislike_count" : post.dislike_count,
        "result" : result
    }

    return HttpResponse(json.dumps(context), content_type = "application/json")

def my_dislike(request, user_id):
    user = User.objects.get(id=user_id)
    dislike_list = Dislike.objects.filter(user = user)
    context = {
        'dislike_list' : dislike_list,
    } 

    return render(request, 'main/my_dislike.html', context)
