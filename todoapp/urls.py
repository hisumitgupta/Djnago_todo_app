from .views import *
from django.urls import path

urlpatterns = [
    path('',index,name='home'),
    path('edit-task/<id>/',edit_task,name='edit_task'),
    path('delete-todo/<id>/',delete_todo,name='delete_todo'),
    path('signup/',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('logout/',user_logout,name='logout'),
    path('search/',search_task,name='search_task'),
]
