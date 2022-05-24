from django.shortcuts import render
from main.models import Blog
from django.contrib.auth.models import User

def mypage(request):
    user=request.user
    blogs=Blog.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'blogs':blogs})

