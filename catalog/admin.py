from django.contrib import admin

from catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'description')


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version_title', 'version_number', 'is_current', 'product')

