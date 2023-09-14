from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=30, verbose_name='заголовок')
    slug = models.CharField(auto_created=150, verbose_name='slug', null=True, blank=True)
    description = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='previews/', verbose_name='превью', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f"{self.title} {self.views_count}"

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
