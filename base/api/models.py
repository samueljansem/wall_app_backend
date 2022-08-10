from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    body = models.TextField(max_length=280, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
