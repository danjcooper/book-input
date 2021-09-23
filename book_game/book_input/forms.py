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

class regester_film_form(ModelForm):
    class Meta:
        model = models.Films
        fields = ['title', 'year', 'director', 'description', 'first_line', 'last_line', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'year': forms.NumberInput(attrs={'placeholder': 'Year'}),
            'director': forms.TextInput(attrs={'placeholder': 'Director'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'first_line': forms.TextInput(attrs={'placeholder': 'First line'}),
            'last_line': forms.TextInput(attrs={'placeholder': 'Last line'}),
            'notes': forms.TextInput(attrs={'placeholder': 'Notes'}),
        }

class regester_album_form(ModelForm):
    class Meta:
        model = models.Albums
        fields = ['title', 'artist', 'year', 'description', 'first_line', 'last_line', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'artist': forms.TextInput(attrs={'placeholder': 'artist'}),
            'year': forms.NumberInput(attrs={'placeholder': 'Year'}),
            'description': forms.Textarea(attrs={'placeholder': 'description'}),
            'first_line': forms.TextInput(attrs={'placeholder': 'First line'}),
            'last_line': forms.TextInput(attrs={'placeholder': 'Last line'}),
            'notes': forms.TextInput(attrs={'placeholder': 'Notes'}),
        }
