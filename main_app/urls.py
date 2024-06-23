from django.urls import path
from . import views
# from todolistapp.views import ToDoList

urlpatterns = [
    path('', views.todo_index, name='home'),
    path('', views.home, name='home'),
    # path('todo/', ToDoList.as_view(), name='todo_index'),
    path('todo/create/', views.TodoCreate.as_view(), name='todo_create'),

]
