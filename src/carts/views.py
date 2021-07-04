from django.db.models.query_utils import Q
from django.shortcuts import render
from django.urls.base import reverse
#from django.db import models
from . import models
from django.views.generic import UpdateView, DetailView, DeleteView, FormView, RedirectView
from django.views import View
from django.http import HttpResponseRedirect
from books import models as books_models
from django.urls import reverse_lazy


class CartView(DetailView):
    template_name = 'carts/cart_edit.html'
    model = models.Cart

    def get_object(self, queryset=None):
        # get cart        
        cart_id = self.request.session.get('cart_id')
        #del self.request.session['cart_id']
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


class CartDeleteView(RedirectView):
    model = models.BooksInCart
    success_url = reverse_lazy('carts:cart_edit')

    def get_redirect_url(self, *args, **kwargs):
        #obj_pk_todelete
        self.model.objects.get(pk=self.kwargs.get('pk')).delete()
        return self.success_url

class CartUpdate(View):
    def post(self, request):
        action = request.POST.get('submit')
        # get cart        
        cart_id = self.request.session.get('cart_id')
        cart, created = models.Cart.objects.get_or_create(    # id of the cart
            pk=cart_id,
            defaults={}
        )
        if created:
            self.request.session['cart_id'] = cart.pk  
        goods = cart.goods.all()
        if goods:
            #def post(self, request):
            for key, value in request.POST.items():
                if 'quantityforgood_' in key:
                    pk = int(key.split('_')[1])
                    good = goods.get(pk=pk)
                    good.quantity = int(value)
                    good.save()
        if action == 'save_cart':            
            return HttpResponseRedirect(reverse_lazy('carts:cart_edit'))
        elif action == 'create_order':
            return HttpResponseRedirect(reverse_lazy('orders:create_order'))
        else:
            return HttpResponseRedirect(reverse_lazy('carts:cart_edit'))




