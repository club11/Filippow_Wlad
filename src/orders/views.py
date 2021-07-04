from django.shortcuts import render
from django.views.generic.edit import FormView
from . import models, forms

from carts import models as carts_models

from django.views.generic import CreateView, FormView, TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.

class CreateOrderView(FormView):
    form_class = forms.OrderCreateForm
    template_name = 'orders/create_order.html'
    success_url = reverse_lazy('orders:success_order')

    def get_initial(self):         #здесь подкидывать данные из profile тел. при подтверждении заказа
        if self.request.user.is_anonymous:
            return {}
        tel = self.request.user.profile.tel
        return {'contact_info': 'contact info', "tel" : tel}

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
        self.request.session.delete('cart_id')
        return super().form_valid(form)

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