from django.db.models import fields
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from . import models

class BookListView(ListView):
    model = models.Book

class BookDetailView(DetailView):
    model = models.Book

class BookCreateView(CreateView):
        model = models.Book
        fields = (
            'name',
            'author',
            'price',
            'line',
            'genre',
            #'publication_date',
            'pages',
            'age_restrictions',
            'publisher',
            'quantity_on_hand',
            'active',
            'rating',
        )

class BookUpdateView(UpdateView):
    model = models.Book
    fields = (
            'name',
            'author',
            'price',
            'line',
            'genre',
            #'publication_date',
            'pages',
            'age_restrictions',
            'publisher',
            'quantity_on_hand',
            'active',
            'rating',
        )

class BookDeleteView(DeleteView):
    model = models.Book
    success_url = reverse_lazy('books_list:books')