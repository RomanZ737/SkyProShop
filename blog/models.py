from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок статьи")
    content = models.TextField(verbose_name="Содержание статьи")
    preview = models.TextField(verbose_name="Краткое содержание статьи")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    views_number = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} {self.preview}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['created_at']