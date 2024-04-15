from django.db import models
from django.urls import reverse
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    author = models.CharField(max_length=100, verbose_name="Автор")
    content = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name="Дата публикации"
    )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])

    def __str__(self):
        return self.title
