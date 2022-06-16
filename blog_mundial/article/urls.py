from django.urls import path
from article import views



urlpatterns = [
    path('article', views.article_list, name='articles'),
    path('article/create', views.article_create, name='article_create')
    ]