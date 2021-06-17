from django.db.models import fields
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from . import models


class HomeListView(ListView):
    model = models.Book
    template_name = 'books/home.html'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 

        in_prerev = models.Book.objects.reverse()           #in pre- reverse

        last_added = in_prerev.order_by('publication_date')[:4] #last_added after reverse
        cheapest = models.Book.objects.order_by('price')[:4] #-----cheapest
        bestsellers = in_prerev.order_by('quantity_on_hand')[:4]

        context['last_added'] = last_added
        context['cheapest'] = cheapest  #order_by('price') ------cheapest
        context['bestsellers'] = bestsellers
        return context







class BookListView(ListView):
    model = models.Book

class BookDetailView(DetailView):
    model = models.Book

class BookCreateView(CreateView):
        model = models.Book
        fields = (
            'picture',
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
           'picture',
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