from django.contrib import admin
from .models import Todo, TodoSubItem

admin.site.register(Todo)
admin.site.register(TodoSubItem)