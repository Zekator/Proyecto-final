from django.urls import path
from country import views


app_name = 'country'
urlpatterns = [
    path('country', views.country_list, name='country_list'),
    path('country/add/', views.country_form, name='country-add'),
    path('country/<int:pk>/update', views.update_country, name='country-update'),
    path('country/<int:pk>/delete', views.delete_country, name='country-delete'),
    ]