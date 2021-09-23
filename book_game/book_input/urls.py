from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('add-a-book/', views.add_book, name="add-a-book"),
    path('add-a-film/', views.add_film, name="add-a-film"),
    path('all/', views.get_all_books, name="all"),
    path('all-films/', views.get_all_films, name="all-films"),
    path('edit-book/<int:id>', views.update_book_entry, name="edit"),
]