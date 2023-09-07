from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=30, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='images/', verbose_name='изображение', null=True, blank=True)
    category = models.CharField(max_length=50, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    created_at = models.DateTimeField(verbose_name='дата создания')
    changed_at = models.DateTimeField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.title} - {self.description}. Цена: {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title} - {self.description}.'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
