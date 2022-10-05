from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=300)
    detail = models.TextField()
    image = models.ImageField(upload_to="posts", null = True)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Answer(models.Model):
    answer = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer
        