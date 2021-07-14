from django.urls import path
from django.conf.urls.static import static
from users import views as users_viesws

from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logged_out/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', users_viesws.Registerview.as_view(), name='register'),
    path('profile_change/', users_viesws.ProfileView.as_view(), name='profile_change'),
    path('admin_portal/', users_viesws.AdminPortalView.as_view(), name='admin_portal'),   
    path('customer_profile_change/<int:pk>/', users_viesws.CustomerProfileView.as_view(), name='customer_profile_change'),
    
]

template_name='users/psd_change.html'
