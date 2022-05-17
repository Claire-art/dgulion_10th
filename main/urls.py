from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', main, name="showmain"),
    path('posts/', posts, name="posts"),
    path('<int:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<int:id>',edit,name='edit'),
    path('update/<int:id>',update,name="update"),
    path('delete/<int:id>' , delete , name='delete'),
]