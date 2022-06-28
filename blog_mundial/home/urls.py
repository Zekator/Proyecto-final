from django.urls import path 
from home import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='main'),
    path('search', views.search, name='search'),
    ]