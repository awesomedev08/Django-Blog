from random import choice
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

import os


CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789'

PERMISSION_CHOICES = (
    (0, 'Anyone can edit '),
    (1, 'Only you and admin can edit')
)


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):


    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body_text = models.TextField()
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, default='', editable=False)
    img = models.ImageField(upload_to='images')
    
    edit_permission = models.IntegerField(choices=PERMISSION_CHOICES, default=1)

    categories = models.ManyToManyField(Category, default='uncategorized')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        
        title = self.title + '-' + ''.join(choice(CHARS) for _ in range(5))
        self.slug = slugify(title, allow_unicode=False)
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ('created_at',)
    
    

class Images(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images')
    name = models.CharField(default='Undefined', max_length=40)

    def __str__(self):
        return self.name