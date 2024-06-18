from django.db import models

# Create your models here.
class Todo(models.Model):
    item = models.CharField(max_length=300)
    subitem = models.CharField(max_length=300)
    date = models.DateField(auto_created=True)
    # time = models.DateTimeField(auto_created=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.item