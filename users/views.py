from django.shortcuts import render
from main.models import Blog
from django.contrib.auth.models import User

def mypage(request):
    user=request.user  
    #로그인한 유저이름과 글 작성자 이름이 동일한 글 필터링
    blogs=Blog.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'blogs':blogs})
