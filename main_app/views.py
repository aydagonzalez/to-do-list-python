from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Todo
from django.views.generic import ListView

class ToDoList(ListView):
    model = Todo

# Define the home view
def home(request):
    return render(request, 'home.html')

def todo_index(request):
    todos = Todo.objects.all() # Retrieve all to-do items
    return render(request, 'home.html', 
    { 
        'todos': todos 
    }
)

class TodoCreate(CreateView):
    model = Todo
    fields = '__all__'
