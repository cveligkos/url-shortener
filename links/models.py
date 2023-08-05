from django.db import models


class Link(models.Model):
    url = models.CharField(max_length=1000, unique=True)
    hash = models.CharField(max_length=255, unique=True)
    visits = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
