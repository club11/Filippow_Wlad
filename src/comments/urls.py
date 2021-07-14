from django.urls import path
from django.conf.urls.static import static

from . import views

app_name = 'comments'
urlpatterns = [
    path('create_comment/', views.CommentCreateView.as_view(), name='create'),
]