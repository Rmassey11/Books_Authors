from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.
class Book(models.Model):
    #id
    title = models.CharField(max_length =255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    #id
    books = models.ManyToManyField(Book, related_name='authors')
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)