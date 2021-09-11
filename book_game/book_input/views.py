from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from . import forms
from . import models

# Create your views here.

def homepage(req):
    return HttpResponse("<h1>Hi</h1>")

def add_book(req):
    if req.method == 'POST':
        sub_form = forms.regester_book_form(req.POST)
        if sub_form.is_valid():
            new_book = sub_form.save()
            return redirect('all')
        return redirect('all')
        
    context = {"form": forms.regester_book_form}
    return render(req, 'add-book.html', context)

def get_all_books(req):
    books = models.Book.objects.all()
    context = {"books": books}
    return render(req, 'all-books.html', context)
