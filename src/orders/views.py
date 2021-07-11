from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from . import models, forms
#from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from carts import models as carts_models

from django.views.generic import CreateView, FormView, TemplateView, UpdateView, DetailView, ListView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

#from project_shop.src import orders
# Create your views here.

class CreateOrderView(FormView):
    form_class = forms.OrderCreateForm
    template_name = 'orders/create_order.html'
    success_url = reverse_lazy('orders:success_order')

    def get_initial(self):         #здесь подкидывать данные из profile тел. при подтверждении заказа
        if self.request.user.is_anonymous:
            return {}
        tel = self.request.user.profile.tel
        #return {'contact_info': "contact info", 'tel' : tel}
        return {'contact_info': tel}


    def form_valid(self, form):
        cart_id = self.request.session.get('cart_id')
        cart, created = carts_models.Cart.objects.get_or_create(    # id of the cart
            pk=cart_id,
            defaults={}
        )
        if created:
            return HttpResponseRedirect(reverse_lazy('carts:cart_edit'))
        ci = form.cleaned_data.get('contact_info')
        order = models.Order.objects.create(
            cart = cart,
            contact_info = ci
        )  

        del self.request.session['cart_id']
        messages.add_message(self.request, messages.INFO, f'{str(self.request.user)}, Ваш заказ принят ')
        #self.request.session.pop('cart_id')
        #return super().form_valid(form)
        return HttpResponseRedirect(reverse_lazy('carts:cart_edit'))


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        cart_id = self.request.session.get('cart_id')
        cart, created = carts_models.Cart.objects.get_or_create(    # id of the cart
            pk=cart_id,
            defaults={}
        )
        context['object'] = cart
        return context


class SuccessOrderView(TemplateView):
    template_name = 'orders/success_order.html'


class OrderListView(ListView):
    model = models.Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        print (context)


        return super().get_context_data(**kwargs)

    def get_queryset(self):
        orders = super().get_queryset()
        #print(orders)
        return orders 

class OrderDeleteView(DeleteView):
    model = models.Order
    success_url = reverse_lazy('orders:order_list')


class OrderUpdateView(UpdateView):
    model = models.Order
    fields = (
        'order_status',
    )
    success_url = reverse_lazy('orders:order_list')

#class OrderDetailView(DetailView):
#    model = models.Order   
