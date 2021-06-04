from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy


from . import models
from . import forms

# Create your views here.

def list_of_reference_books(request):
    return render(request, template_name='list_of_reference_books.html', context={})

class BookRef(TemplateView):
    template_name = 'book_guide/list_of_reference_books.html'


class GenreListView(ListView):
    model = models.Genre  

class GenreDetailView(DetailView):
    model = models.Genre

class GenreUpdateView(UpdateView):
    model = models.Genre
    fields = (
        'name',
    )

class GenreCreateView(CreateView):
    model = models.Genre
    fields = (
        'name',
    )

class GenreDeleteView(DeleteView):
    model = models.Genre
    success_url = reverse_lazy('genres')

class AuthorListView(ListView):
    model = models.Author

class AuthorDetailView(DetailView):
    model = models.Author
  
class AuthorUpdateView(UpdateView):
    model = models.Author
    fields = (
        'name',
    )

class AuthorCreateView(CreateView):
    model = models.Author
    fields = (
        'name',
    )

class AuthorDeleteView(DeleteView):
    model = models.Author
    success_url = reverse_lazy('authors')

class LineListView(ListView):
    model = models.Line

class LineDetailView(DetailView):
    model = models.Line

class LineUpdateView(UpdateView):
    model = models.Line
    fields = (
        'name',
    )
    
class LineCreateView(CreateView):
    model = models.Line
    fields = (
        'name',
    )

class LineDeleteView(DeleteView):
    model = models.Line
    success_url = reverse_lazy('lines')

class PublisherListView(ListView):
    model = models.Publisher

class PublisherDetailView(DetailView):
    model = models.Publisher
 
class PublisherUpdateView(UpdateView):
    model = models.Publisher
    fields = (
        'name',
    )

class PublisherCreateView(CreateView):
    model = models.Publisher
    fields = (
        'name',
    )

class PublisherDeleteView(DeleteView):
    model = models.Publisher
    success_url = reverse_lazy('publishers')


def book(request, book_id):
    book = models.Book.objects.get(pk=book_id)
    ctx = {
        'book' : book
    }
    return render(request, template_name='book_detail.html', context=ctx) 
    