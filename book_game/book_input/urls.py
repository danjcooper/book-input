from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('add-a-book/', views.add_book, name="add-a-book"),
    path('all/', views.get_all_books, name="all"),
    path('edit-book/<int:id>', views.update_book_entry, name="edit"),
]