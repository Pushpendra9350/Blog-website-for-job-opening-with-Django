from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# This our post model to store posts 
class Post(models.Model):
    """
    # Here we are using only 100 length content for the title of the blog post
    # TextField is used for the lengthy text
    # DateTimeField(auto_now=True)  when we update next time our post then it will update to the current date every time 
    # DateTimeField(auto_now_add=True) it set dateand time to the time when it object is created but we can not update it.
    # DateTimeField(default=timezone.now) now we can also update the date time of the post when we want 
    # User and Post will be in the one to many relation ship when we delete a user the all posts will be delete
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})