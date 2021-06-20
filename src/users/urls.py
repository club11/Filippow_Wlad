from django.urls import path
from django.conf.urls.static import static
from users import views as users_viesws

from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('login/', users_viesws.MyLoginView.as_view(), name='userlogin'),
    path('passwordchange/', users_viesws.MyLoginPasswordChangeView.as_view(), name='passwrdchnge'),
    #path('userprofile/', users_viesws.UserProfileDetailView.as_view(), name='userprofile'),
]