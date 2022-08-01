from django.shortcuts import render, get_object_or_404, redirect
from main.models import Blog
from django.contrib.auth.models import User

# Create your views here.
def mypage(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    posts = Blog.objects.filter(writer=user)
    
    return render(request, 'users/mypage.html',
    {'posts' : posts, 
    'user': user, 
    'followings' : user.profile.followings.all(),
    'followers' : user.profile.followers.all()
    })

def follow(request, user_id):
    user = request.user
    followed_user = get_object_or_404(User, pk=user_id)
    is_follower = user.profile in followed_user.profile.followers.all()

    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('users:mypage', followed_user.id)