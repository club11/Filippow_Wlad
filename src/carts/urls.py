from django.urls import path
from django.conf.urls.static import static
from carts import views as carts_views



app_name = 'carts'

urlpatterns = [
    path('', carts_views.CartView.as_view(), name='cart_edit'),


]