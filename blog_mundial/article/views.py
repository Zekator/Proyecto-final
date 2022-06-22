from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from article.models import Article
# Create your views here.

class ArticleCreateView(CreateView):
    model = Article
    success_url = reverse_lazy('article:article_list')
    fields = ['name', 'country', 'article_id', 'article_content']
    

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    

class ArticleUpdateView(UpdateView):
    model = Article
    success_url = reverse_lazy('article:article_list')
    fields = ['name', 'country', 'article_id', 'article_content']
    
    
class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('article:article_list')
    
    


