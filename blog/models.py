from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class Comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)


