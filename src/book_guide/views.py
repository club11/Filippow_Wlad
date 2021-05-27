from django.shortcuts import render
from . import models

# Create your views here.

def genre_list(request):
    genre_list = models.Genre.objects.all()
    ctx = {
        'genre_list' : genre_list
    }
    return render(request, template_name='genre_list.html', context=ctx)


def author_list(request):
    author_list = models.Author.objects.all()
    ctx = {
        'author_list' : author_list
    }
    return render(request, template_name='author_list.html', context=ctx)    

def lines_list(request):
    lines_list = models.Line.objects.all()
    ctx = {
        'lines_list' : lines_list
    }
    return render(request, template_name='lines_list.html', context=ctx) 

def publishers_list(request):
    publishers_list = models.Publisher.objects.all()
    ctx = {
        'publishers_list' : publishers_list
    }
    return render(request, template_name='publishers_list.html', context=ctx) 

def book(request, book_id):
    book = models.Book.objects.get(pk=book_id)
    ctx = {
        'book' : book
    }
    return render(request, template_name='book_detail.html', context=ctx) 
    