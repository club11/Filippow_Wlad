from django.db.models.query_utils import Q
from django.shortcuts import render
from . import models
from django.views.generic import UpdateView, DetailView
from books import models as books_models

class CartView(DetailView):
    template_name = 'carts/cart_edit.html'
    model = models.Cart

    def get_object(self, queryset=None):
        # get cart      
        cart_id = self.request.session.get('cart_id')
        cart, created = models.Cart.objects.get_or_create(    # id of the cart
            pk=cart_id,
            defaults={}
        )
        if created:
            self.request.session['cart_id'] = cart.pk
        #get book_in_cart
        book_id=self.request.GET.get('book.pk')
        if book_id:
            book = books_models.Book.objects.get(pk=int(book_id))
            book_in_cart, book_created = models.BooksInCart.objects.get_or_create(   
            cart=cart,
            book=book,
            defaults={
                'unit_price':book.price
            }
        )
            if not book_created:
                # prod position in the cart
                q = book_in_cart.quantity + 1
                book_in_cart.quantity = q
                book_in_cart.save()
            #else:
            #    book_in_cart.unit_price = book.price
        return cart

    def get_context_data(self, **kwargs): 
        book_id=self.request.GET.get('book.pk')
        context = super().get_context_data(**kwargs) 
        qs = models.Cart.objects.get(book_id)
        context['qs'] = qs 
        return context



class BooksInCartView(DetailView):
    model = models.BooksInCart
    template_name = 'carts/book_in_cart.html'