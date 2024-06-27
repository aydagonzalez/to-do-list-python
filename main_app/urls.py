from django.urls import path
from . import views
# from todolistapp.views import ToDoList

urlpatterns = [
    path('', views.todo_index, name='home'),
    path('', views.home, name='home'),
    path('todo/create/', views.todo_create, name='todo_create'),
    path('todo/subitem/create/', views.todo_subitem_create, name='todo_subitem_create'),
    path('todo/<int:pk>/update', views.todo_update, name='todo_update'),
    path('todo/<int:pk>/delete', views.todo_delete, name='todo_delete'),
    # path('todo/<int:pk>/update', views.TodoUpdate.as_view(), name='todo_update'),
    # path('todo/create/', views.TodoCreate.as_view(), name='todo_create'),
    # path('todo/<int:pk>/delete', views.TodoDelete.as_view(), name='todo_delete'),

]
