from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_index, name='home'),
    path('', views.home, name='home'),
]
