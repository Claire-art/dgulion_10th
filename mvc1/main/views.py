import re
from django.shortcuts import render

# mainpage view 함수

def showmain(request):
    return render(request, 'main/mainpage.html')

# firstpage view 함수
def showfirst(request):
    return render(request , 'main/firstpage.html')


# secondpage view 함수
def showsecond(request):
    return render(request,'main/secondpage.html')

