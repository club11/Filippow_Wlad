from django.urls import path
from django.conf.urls.static import static
from carts import views as carts_views



app_name = 'carts'

urlpatterns = [
    path('', carts_views.CartView.as_view(), name='cart_edit'),
    path('delete_good_in_cart/<int:pk>', carts_views.CartDeleteView.as_view(), name='delete_good_in_cart'),
    path('update_good_in_cart/', carts_views.CartUpdate.as_view(), name='update_good_in_cart'),

]