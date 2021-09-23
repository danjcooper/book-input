from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from . import forms
from . import models

# Create your views here.

def homepage(req):
    return HttpResponse("<h1>Hi</h1>")

def add_book(req):

    form = forms.regester_book_form(req.POST or None)
    error_message = None

    if req.method == 'POST' and form.is_valid():
        all_entries = models.Book.objects.all()
        try:
            for book in all_entries:
                if form.cleaned_data["title"] == book.title:
                    error_message = 'Book already exists'
                    raise Exception()
            form.save()
            return redirect('all')
        except Exception:
            pass
        
    context = {"form": form, "error": error_message}
    return render(req, 'add-book.html', context)

def get_all_books(req):
    books = models.Book.objects.all().order_by("-pk")
    context = {"books": books}
    return render(req, 'all-books.html', context)

def update_book_entry(req, id):
    instance = get_object_or_404(models.Book, id=id)
    form = forms.regester_book_form(req.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('all')
    return render(req, 'update-book.html', {'form': form}) 


def add_film(req):
    
    form = forms.regester_film_form(req.POST or None)
    error_message = None

    if req.method == 'POST' and form.is_valid():
        all_entries = models.Films.objects.all()
        try:
            for book in all_entries:
                if form.cleaned_data["title"] == book.title:
                    error_message = 'Film already exists'
                    raise Exception()
            form.save()
            return redirect('all-films')
        except Exception:
            pass
        
    context = {"form": form, "error": error_message}
    return render(req, 'add-film.html', context)

def get_all_films(req):
    films = models.Films.objects.all().order_by("-pk")
    context = {"films": films}
    return render(req, 'all-films.html', context)