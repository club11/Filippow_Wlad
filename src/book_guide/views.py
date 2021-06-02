from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from . import models
from . import forms

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



def genre_update(request, genre_id):
    if request.method == "POST":
        obj = models.Genre.objects.get(pk=genre_id)
        form = forms.CreateGenreForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('genres'))
        else:
            pass
    else:
        obj = models.Genre.objects.get(pk=genre_id)
        form = forms.CreateGenreForm(instance=obj)
    ctx = {
        'form' : form,
        'is_valid' : form.is_valid()
    }
    return render(request, template_name='genre_update.html', context=ctx) 

    
def genre_create(request):
    if request.method == "POST":
        form = forms.CreateGenreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('genres'))
        else:
            pass
    else:
        form = forms.CreateGenreForm()
    ctx = {
        'form' : form,
        'is_valid' : form.is_valid()
    }
    return render(request, template_name='genre_create.html', context=ctx) 


def genre_delete(request, genre_id):
    if request.method == "POST":
        obj = models.Genre.objects.get(pk=genre_id).delete()
        return HttpResponseRedirect(reverse('genres'))
    return render(request, template_name='genre_delete.html', context={})

























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

def author_update(request, author_id):
    if request.method == "POST":
        obj = models.Author.objects.get(pk=author_id)
        form = forms.CreateAuthorForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authors'))
        else:
            pass
    else:
        obj = models.Author.objects.get(pk=author_id)
        form = forms.CreateAuthorForm(instance=obj)
    ctx = {
        'form' : form,
        'is_valid' : form.is_valid()
    }
    return render(request, template_name='author_update.html', context=ctx) 

    
def author_create(request):
    if request.method == "POST":
        form = forms.CreateAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authors'))
        else:
            pass
    else:
        form = forms.CreateAuthorForm()
    ctx = {
        'form' : form,
        'is_valid' : form.is_valid()
    }
    return render(request, template_name='author_create.html', context=ctx) 


def author_delete(request, author_id):
    if request.method == "POST":
        obj = models.Author.objects.get(pk=author_id).delete()
        return HttpResponseRedirect(reverse('authors'))
    return render(request, template_name='author_delete.html', context={})


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

def line_update(request, line_id):
    if request.method == "POST":
        obj = models.Line.objects.get(pk=line_id)
        form = forms.CreateLineForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lines'))
        else:
            pass
    else:
        obj = models.Line.objects.get(pk=line_id)
        form = forms.CreateLineForm(instance=obj)
    ctx = {
        'form' : form,
        'is_valid' : form.is_valid()
    }
    return render(request, template_name='line_update.html', context=ctx) 

    
def line_create(request):
    if request.method == "POST":
        form = forms.CreateLineForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lines'))
        else:
            pass
    else:
        form = forms.CreateLineForm()
    ctx = {
        'form' : form,
        'is_valid' : form.is_valid()
    }
    return render(request, template_name='line_create.html', context=ctx) 


def line_delete(request, line_id):
    if request.method == "POST":
        obj = models.Line.objects.get(pk=line_id).delete()
        return HttpResponseRedirect(reverse('lines'))
    return render(request, template_name='line_delete.html', context={})


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

def publisher_update(request, publisher_id):
    if request.method == "POST":
        obj = models.Publisher.objects.get(pk=publisher_id)
        form = forms.CreatePublisherForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('publishers'))
        else:
            pass
    else:
        obj = models.Publisher.objects.get(pk=publisher_id)
        form = forms.CreatePublisherForm(instance=obj)
    ctx = {
        'form' : form,
        'is_valid' : form.is_valid()
    }
    return render(request, template_name='publisher_update.html', context=ctx) 

    
def publisher_create(request):
    if request.method == "POST":
        form = forms.CreatePublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('publishers'))
        else:
            pass
    else:
        form = forms.CreatePublisherForm()
    ctx = {
        'form' : form,
        'is_valid' : form.is_valid()
    }
    return render(request, template_name='publisher_create.html', context=ctx) 


def publisher_delete(request, publisher_id):
    if request.method == "POST":
        obj = models.Publisher.objects.get(pk=publisher_id).delete()
        return HttpResponseRedirect(reverse('publishers'))
    return render(request, template_name='publisher delete.html', context={})




def book(request, book_id):
    book = models.Book.objects.get(pk=book_id)
    ctx = {
        'book' : book
    }
    return render(request, template_name='book_detail.html', context=ctx) 
    