from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from catalog.models import Product, Contact


# Create your views here.

class ProductListView(ListView):
    model = Product


class ContactCreateView(CreateView):
    model = Contact
    fields = ('name', 'phone_number', 'message',)
    success_url = reverse_lazy('catalog:contacts')


class ProductDetailView(DetailView):
    model = Product




