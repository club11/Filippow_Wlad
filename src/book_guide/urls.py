from django.urls import path
from django.conf.urls.static import static
from book_guide import views as books_viesws

app_name = 'book_guide'


urlpatterns = [
    path('book_references/', books_viesws.BookRef.as_view(), name="book_references"), 
    path('genre/', books_viesws.GenreListView.as_view(), name="genres"),
    path('genre_detail/<int:pk>/', books_viesws.GenreDetailView.as_view(), name="genre_data"),
    path('genre_create/', books_viesws.GenreCreateView.as_view(), name="genre_create"),
    path('genre_update/<int:pk>/', books_viesws.GenreUpdateView.as_view(), name="genre_update"),
    path('genre_delete/<int:pk>/', books_viesws.GenreDeleteView.as_view(), name="genre_delete"),

    path('author/', books_viesws.AuthorListView.as_view(), name="authors"),
    path('author_detail/<int:pk>/', books_viesws.AuthorDetailView.as_view(), name="author_detail"),
    path('author_create/', books_viesws.AuthorCreateView.as_view(), name="author_create"),
    path('author_update/<int:pk>/', books_viesws.AuthorUpdateView.as_view(), name="author_update"),
    path('author_delete/<int:pk>/', books_viesws.AuthorDeleteView.as_view(), name="author_delete"),
    
    path('line/', books_viesws.LineListView.as_view(), name="lines"),
    path('lines_detail/<int:pk>/', books_viesws.LineDetailView.as_view(), name="lines_data"),
    path('line_create/', books_viesws.LineCreateView.as_view(), name="line_create"),
    path('line_update/<int:pk>/', books_viesws.LineUpdateView.as_view(), name="line_update"),
    path('line_delete/<int:pk>/', books_viesws.LineDeleteView.as_view(), name="line_delete"),

    path('publisher/', books_viesws.PublisherListView.as_view(), name="publishers"),
    path('publisher_data/<int:pk>/', books_viesws.PublisherDetailView.as_view(), name="publisher_data"),
    path('publisher_create/', books_viesws.PublisherCreateView.as_view(), name="publisher_create"),
    path('publisher_update/<int:pk>/', books_viesws.PublisherUpdateView.as_view(), name="publisher_update"),
    path('publisher_delete/<int:pk>/', books_viesws.PublisherDeleteView.as_view(), name="publisher_delete"),
]