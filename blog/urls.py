from django.urls import path
from .views import BlogListView, AboutPageView, BlogDetailView


urlpatterns = [
    path('',BlogListView.as_view(), name= 'home'),
    path('about/',AboutPageView.as_view(), name= 'about'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name= 'post_detail'),
]

