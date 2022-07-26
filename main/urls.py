from django.urls import path
from .views import *
from main import views

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
    path('<str:blog_id>/create_comment', create_comment, name="create_comment"),
    path('delete_comment/<int:id>', delete_comment, name="delete_comment"),
    path('edit_comment/<int:id>', edit_comment, name="edit_comment"),
    path('update_comment/<int:id>', update_comment, name="update_comment"),

]