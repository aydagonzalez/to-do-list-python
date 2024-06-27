from django.db import models
from django.urls import reverse

class Todo(models.Model):
    item = models.CharField(max_length=300)
    subitem = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)  
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.item} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('home')

class TodoSubItem(models.Model):
    task_subitem = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True) 
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.task_subitem} (Parent ID: {self.todo.id})'
