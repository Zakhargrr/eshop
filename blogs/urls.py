from django.urls import path

from blogs.apps import BlogsConfig

from blogs.views import BlogCreateView, BlogListView, BlogUpdateView, BlogDetailView, BlogDeleteView

app_name = BlogsConfig.name
urlpatterns = [
    path('list/', BlogListView.as_view(), name='list'),
    path('create_blog/', BlogCreateView.as_view(), name='create_blog'),
    path('blog_info/<int:pk>/', BlogDetailView.as_view(), name='blog_info'),
    path('edit_blog/<int:pk>/', BlogUpdateView.as_view(), name='edit_blog'),
    path('delete_blog/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
]
