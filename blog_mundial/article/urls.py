from django.urls import path
from article import views


app_name = 'article'
urlpatterns = [
    path('article', views.ArticleListView.as_view(), name='article_list'),
    path('article/create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/detail', views.ArticleDetailView.as_view(), name='article-detail'),
    path('article/<int:pk>/update', views.ArticleUpdateView.as_view(), name='article-update'),
    path('article/<int:pk>/delete', views.ArticleDeleteView.as_view(), name='article-delete'),
    ]
    