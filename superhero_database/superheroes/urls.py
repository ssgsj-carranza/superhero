from . import views
from django.urls import path

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superheroes_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_superhero'),
    path('delete/', views.delete, name='id')
]