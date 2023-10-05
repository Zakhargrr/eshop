from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactCreateView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name
urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactCreateView.as_view(), name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('create-product/', ProductCreateView.as_view(), name='create_product'),
    path('edit-product/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('delete-product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product')
]
