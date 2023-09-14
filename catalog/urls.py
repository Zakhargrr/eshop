from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactCreateView, ProductDetailView

app_name = CatalogConfig.name
urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactCreateView.as_view(), name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
]
