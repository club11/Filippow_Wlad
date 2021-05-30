from django.shortcuts import render
from . import models

# Create your views here.

def list_of_reference_books(request):
    return render(request, template_name='list_of_reference_books.html', context={})


def genre_list(request):
    genre_list = models.Genre.objects.all()
    ctx = {
        'genre_list' : genre_list
    }
    return render(request, template_name='genre_list.html', context=ctx)

def genre_data(request, genre_id):
    genre_data = models.Genre.objects.get(pk=genre_id)
    ctx = {
        'genre_data' : genre_data
    }
    return render(request, template_name='genre_data.html', context=ctx)    


def author_list(request):
    author_list = models.Author.objects.all()
    ctx = {
        'author_list' : author_list
    }
    return render(request, template_name='author_list.html', context=ctx)   

def author_data(request, author_id):
    author_data = models.Author.objects.get(pk=author_id)
    ctx = {
        'author_data' : author_data
    }
    return render(request, template_name='author_data.html', context=ctx) 

def lines_list(request):
    lines_list = models.Line.objects.all()
    ctx = {
        'lines_list' : lines_list
    }
    return render(request, template_name='lines_list.html', context=ctx) 

def lines_list_data(request, lines_id):
    lines_list_data = models.Line.objects.get(pk=lines_id)
    ctx = {
        'lines_list_data' : lines_list_data
    }
    return render(request, template_name='lines_data.html', context=ctx) 

def publishers_list(request):
    publishers_list = models.Publisher.objects.all()
    ctx = {
        'publishers_list' : publishers_list
    }
    return render(request, template_name='publishers_list.html', context=ctx) 



def publisher_data(request, publisher_id):
    publisher_data = models.Publisher.objects.get(pk=publisher_id)
    ctx = {
        'publisher_data' : publisher_data
    }
    return render(request, template_name='publisher_data.html', context=ctx) 


def book(request, book_id):
    book = models.Book.objects.get(pk=book_id)
    ctx = {
        'book' : book
    }
    return render(request, template_name='book_detail.html', context=ctx) 
    