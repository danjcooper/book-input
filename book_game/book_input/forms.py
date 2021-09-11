from django.forms import ModelForm
from django import forms
from . import models


class regester_book_form(ModelForm):
    class Meta:
        model = models.Book
        fields = ['title', 'author', 'year', 'blurb', 'first_line', 'last_line', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author'}),
            'year': forms.NumberInput(attrs={'placeholder': 'Year'}),
            'blurb': forms.Textarea(attrs={'placeholder': 'Blurb'}),
            'first_line': forms.TextInput(attrs={'placeholder': 'First line'}),
            'last_line': forms.TextInput(attrs={'placeholder': 'Last line'}),
            'notes': forms.TextInput(attrs={'placeholder': 'Notes'}),
        }
