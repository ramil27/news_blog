from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-create_at']


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Meta:
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'
    ordering = ['title']
