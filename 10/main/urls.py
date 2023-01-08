
from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', main, name="showmain"),
    path('<str:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('posts/', posts, name="posts"),
    path('edit/<str:id>',edit,name="edit"),
    path('update/<str:id>',update,name="update"),
    path('delete/<str:id>',delete,name="delete"),
]