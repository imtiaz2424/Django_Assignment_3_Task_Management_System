from django.db import models
from categories.models import Category
from author.models import Author

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    is_completed = models.BooleanField(default='False')
    assign_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
