from django.urls import path
from django.conf.urls.static import static
from orders import views as orders_views



app_name = 'orders'

urlpatterns = [
    path('create_order/', orders_views.CreateOrderView.as_view(), name='create_order'),
    path('success_order/', orders_views.SuccessOrderView.as_view(), name='success_order'),

]