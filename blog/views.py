from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView,CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy 

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView): # new
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']    

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'post_edit.html'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')