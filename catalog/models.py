from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title} - {self.description}.'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    title = models.CharField(max_length=30, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='images/', verbose_name='изображение', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.PositiveIntegerField(verbose_name='цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    changed_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.title} - {self.description}. Цена: {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Contact(models.Model):
    name = models.CharField(max_length=30, verbose_name='имя')
    phone_number = models.CharField(verbose_name='номер телефона')
    message = models.TextField(verbose_name='сообщение')

    def __str__(self):
        return f"{self.name} {self.phone_number}"

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


