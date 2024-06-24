from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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


class TodoUpdate(UpdateView):
    model = Todo
    fields = '__all__'

# class TodoDelete(DeleteView):
#     model = Todo
#     success_url = '/'


# listings/views.py

def todo_update(request, pk):
    # pass
    print("HELLOOOOOOOOOOOO !")
    print('THIS IS THE REQUEST:',request, "THIS IS PK", pk)
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance = todo) # prepopulates the form with an existing data
    return render(request,
                  'home.html',
                  {'form': form})
    



def todo_delete(request, pk):
    # print("HELLOOOOOOOOOOOO !")
    # print('THIS IS THE REQUEST:',request, "THIS IS PK", pk)
    todo = Todo.objects.get(id=pk) # we need this for both GET and POST
    # print("GOOOOOOOOODBYE!")
    # print (todo)
    if request.method == 'POST':
        # delete the band from the database
        todo.delete()
        # redirect to the bands list
        return redirect('home')
    # no need for an `else` here. If it's a GET request, just continue
    return render(request,
                    'home.html')
