from django.db.models import fields
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
#from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from . import models



class BookListView(ListView):
    model = models.Book


class BookDetailView(DetailView):
    model = models.Book

#class BookCreateView(LoginRequiredMixin, CreateView):
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
    #login_url = '/login/'
    #redirect_field_name = 'redirect_to'        

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


class BookDeleteViiew(DeleteView):
    model= models.Book
    success_url = reverse_lazy('books_list:book_list')

#class BookDeleteView(PermissionRequiredMixin, DeleteView):
#    model = models.Book
#    #login_url = '/login/'
#    #permission_required = 'books.delete_book'
#    success_url = reverse_lazy('books_list:books')

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


#class HomeListViewCustomer(LoginRequiredMixin, ListView):
class HomeListViewCustomer(ListView):
    model = models.Book
    template_name = 'books/home_customer.html'

    #login_url = '/login/'
    #redirect_field_name = 'redirect_to' 

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
        


class BookListCustomerView(ListView):
    model = models.Book
    template_name = 'books/book_list_customer.html'

class BookDetailCustomerView(DetailView):
    model = models.Book    
    template_name = 'books/book_detail_customer.html'





