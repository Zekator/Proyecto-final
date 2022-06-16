from django.urls import path
from country import views



urlpatterns = [
    path('country', views.country_list, name='countries'),
    path('country/add', views.country_add, name='country_add'),
    ]