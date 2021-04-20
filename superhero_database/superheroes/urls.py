from . import views
from django.urls import path

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:superhero_id>', views.detail, name='detail'),
    path('create/', views.create, name='create_new_superhero'),
    path('delete/<int:superhero_id>', views.delete, name='delete'),
    path('update_hero/<int:superhero_id>', views.update_hero, name='update_hero')
]