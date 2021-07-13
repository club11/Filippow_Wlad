from django.urls import path
from django.conf.urls.static import static
from users import views as users_viesws

from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logged_out/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', users_viesws.Registerview.as_view(), name='register'),
    #path('pass_change/', auth_views.PasswordChangeView.as_view(template_name='pass_change.html'), name='pass_change'),

    #path('profile/', users_viesws.ProfileView.as_view(), name='profile'),

    path('profile_change/', users_viesws.ProfileView.as_view(), name='profile_change'),
    
    path('customer_profile_change/<int:pk>/', users_viesws.CustomerProfileView.as_view(), name='customer_profile_change'),
    
]

template_name='users/psd_change.html'


    #path('psd_change/', users_viesws.MyLoginPasswordChangeView.as_view(template_name = 'users/psd_change.html'), name='psd_change'),
    #path('psd_change-done/', users_viesws.MyLoginPasswordChangeDoneView.as_view(), name='psd_change-done'),
    #path('psd_change/', users_viesws.MyLoginPasswordChangeView.as_view(), name='psd_change'),
    #path('userprofile/', users_viesws.UserProfileDetailView.as_view(), name='userprofile'),