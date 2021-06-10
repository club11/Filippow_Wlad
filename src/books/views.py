from django.db.models import fields
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from . import models

class BookListView(ListView):
    model = models.Book

class BookDetailView(DeleteView):
    model = models.Book
    fields = (
        'name',
        'author',
        'line',
        'genre',
        'publication_date',
        'pages',
        'age_restrictions',
        'publisher',
        'quantity_on_hand',
        'active',
        'rating',
    )


def book(request, book_id):
    book = models.Book.objects.get(pk=book_id)
    ctx = {
        'book' : book
    }
    return render(request, template_name='book_detail.html', context=ctx) 