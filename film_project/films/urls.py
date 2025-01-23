from django.urls import path
from . import views

urlpatterns = [
    path('', views.film_list, name='film_list'),
    path('<int:pk>/', views.film_detail, name='film_detail'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add-film/', views.add_film, name='add_film'),
    path('edit-film/<int:film_id>/', views.edit_film, name='edit_film'),
    path('delete-film/<int:film_id>/', views.delete_film, name='delete_film'),

]
