from django.urls import path
from django.conf.urls.static import static
from users import views as users_viesws

from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    #path('login/', users_viesws.MyLoginView.as_view(), name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logged_out/', auth_views.LogoutView.as_view(), name='logged_out'),
    path('register/', users_viesws.Registerview.as_view(), name='register'),
    


    #path('passwordchange/', users_viesws.MyLoginPasswordChangeView.as_view(), name='passwrdchnge'),
    #path('userprofile/', users_viesws.UserProfileDetailView.as_view(), name='userprofile'),
]