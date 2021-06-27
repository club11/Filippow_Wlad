from django.db.models.query_utils import Q
from django.shortcuts import render
#from django.db import models
from . import models
from django.views.generic import UpdateView, DetailView
from books import models as books_models
#from ..books import models as books_models


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
        object_id=self.request.GET.get('object_id')
        if object_id:
            book = books_models.Book.objects.get(pk=int(object_id))
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


