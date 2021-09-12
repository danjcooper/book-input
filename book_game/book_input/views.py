from django.shortcuts import render, redirect
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
                print(form.cleaned_data["title"])
                print(book.title)
                if form.cleaned_data["title"] == book.title:
                    error_message = 'Book already exists'
                    raise Exception()
            form.save()
            return redirect('all')
        except Exception:
            print(Exception.args)
            pass
        
    context = {"form": form, "error": error_message}
    return render(req, 'add-book.html', context)

def get_all_books(req):
    books = models.Book.objects.all()
    context = {"books": books}
    return render(req, 'all-books.html', context)
