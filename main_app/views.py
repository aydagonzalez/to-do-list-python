from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Todo, TodoSubItem
from django.views.generic import ListView
from django import forms
from django.forms import formset_factory



class ToDoList(ListView):
    model = Todo

# Define the home view
def home(request):
    return render(request, 'home.html')

def todo_index(request):
    todo_create_form = TodoForm()
    todo_sub_item_create_form = TodoSubItemForm()
    todos = Todo.objects.all() # Retrieve all to-do items
    todo_subitems = TodoSubItem.objects.all() # Retrieve all to-do items
    return render(request, 'home.html', 
    { 
        'todos': todos,
        'todo_subitems': todo_subitems,
        'todo_create_form': todo_create_form,
        'todo_sub_item_create_form': todo_sub_item_create_form,
    }
)

class TodoCreate(CreateView):
    model = Todo
    fields = '__all__'

class TodoSubItemCreate(CreateView):
    model = TodoSubItem
    fields = '__all__'

# class TodoUpdate(UpdateView):
#     model = Todo
#     fields = '__all__'

# class TodoDelete(DeleteView):
#     model = Todo
#     success_url = '/'


# listings/views.py

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

class TodoSubItemForm(forms.ModelForm):
    class Meta:
        model = TodoSubItem
        fields =  '__all__'

def todo_create(request):
    print("RESQEUS", request)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('home')
    
def todo_subitem_create(request):
    print("RESQEUS", request)
    if request.method == 'POST':
        form = TodoSubItemForm(request.POST)
        if form.is_valid():
            todo_sub_item = form.save()
            return redirect('home')
    

def todo_update(request, pk):
    # print("HELLOOOOOOOOOOOO !")
    # print('THIS IS THE REQUEST:',request, "THIS IS PK", pk)
    todo = Todo.objects.get(id=pk)
    # print("TO Do:", todo)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        form_update = TodoForm(instance = todo) # prepopulates the form with an existing data
    print("TO Do:form_update", form_update)
    return render(request,
                  'home.html',
                  {'form_update': form_update},
                #   {'form': form}
                  )
    



def todo_delete(request, pk):
    todo = Todo.objects.get(id=pk) # we need this for both GET and POST
    if request.method == 'POST':
        # delete the task from the database
        todo.delete()
        # redirect to the bands list
        return redirect('home')
    # no need for an `else` here. If it's a GET request, just continue
    return render(request,
                    'home.html')
