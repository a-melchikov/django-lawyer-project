from django.db import models
from django.urls import reverse
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])

    def __str__(self):
        return self.title
