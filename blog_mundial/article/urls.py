from django.urls import path
from article import views
from django.conf.urls import include

app_name = 'article'
urlpatterns = [
    path('article', views.article_list, name='article_list'),
    path('article/add/', views.article_form, name='article_form'),
    path('article/<int:pk>/detail', views.article_detail, name='article-detail'),
    # path('article/<int:pk>/update', views.ArticleUpdateView.as_view(), name='article-update'),
    # path('article/<int:pk>/delete', views.ArticleDeleteView.as_view(), name='article-delete'),
    path(r'ckeditor/', include('ckeditor_uploader.urls')),
    ]
    