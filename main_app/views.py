from django.shortcuts import render
from .models import Todo

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

