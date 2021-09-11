from django.forms import ModelForm
from django import forms
from . import models


class regester_book_form(ModelForm):
    class Meta:
        model = models.Book
        fields = ['title', 'author', 'year', 'blurb', 'first_line', 'last_line', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'})
        }
