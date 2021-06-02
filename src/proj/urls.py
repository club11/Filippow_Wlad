"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from aeroports import views as airport_names_views
from book_guide import views as books_viesws

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_of_reference_books/', books_viesws.list_of_reference_books, name="list_of_reference_books"),
    path('book/<int:book_id>/', books_viesws.book, name="books"),
    path('genre/', books_viesws.genre_list, name="genres"),
    path('genre_data/<int:genre_id>/', books_viesws.genre_data, name="genre_data"),

    path('genre_create/', books_viesws.genre_create, name="genre_create"),
    path('genre_update/<int:genre_id>/', books_viesws.genre_update, name="genre_update"),
    path('genre_delete/<int:genre_id>/', books_viesws.genre_delete, name="genre_delete"),

    path('author/', books_viesws.author_list, name="authors"),
    path('author_data/<int:author_id>/', books_viesws.author_data, name="author_data"),

    path('author_create/', books_viesws.author_create, name="author_create"),
    path('author_update/<int:author_id>/', books_viesws.author_update, name="author_update"),
    path('author_delete/<int:author_id>/', books_viesws.author_delete, name="author_delete"),
    
    path('line/', books_viesws.lines_list, name="lines"),
    path('lines_data/<int:lines_id>/', books_viesws.lines_list_data, name="lines_data"),

    path('line_create/', books_viesws.line_create, name="line_create"),
    path('line_update/<int:line_id>/', books_viesws.line_update, name="line_update"),
    path('line_delete/<int:line_id>/', books_viesws.line_delete, name="line_delete"),

    path('publisher/', books_viesws.publishers_list, name="publishers"),
    path('publisher_data/<int:publisher_id>/', books_viesws.publisher_data, name="publisher_data"),
    path('publisher_create/', books_viesws.publisher_create, name="publisher_create"),
    path('publisher_update/<int:publisher_id>/', books_viesws.publisher_update, name="publisher_update"),
    path('publisher_delete/<int:publisher_id>/', books_viesws.publisher_delete, name="publisher_delete"),
    path('list_of_cities/',airport_names_views.cities_list),
    path('<airport_code>/', airport_names_views.airport_city),
    path('', airport_names_views.home_page),
]
