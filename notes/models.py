from django.db import models
from categories.models import Category

class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name='notes')

    def __str__(self):
        return self.title