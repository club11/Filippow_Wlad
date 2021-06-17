from django.urls import path
from django.conf.urls.static import static
from books import views as books_book_viesws

app_name = 'books'

urlpatterns = [
    path('home/', books_book_viesws.HomeListView.as_view(), name="home"),

    path('books/', books_book_viesws.BookListView.as_view(), name="books"),
    path('book_detail/<int:pk>/', books_book_viesws.BookDetailView.as_view(), name="book_detail"),
    path('book_create/', books_book_viesws.BookCreateView.as_view(), name="book_create"),
    path('book_update/<int:pk>/', books_book_viesws.BookUpdateView.as_view(), name="book_update"),
    path('book_delete/<int:pk>/', books_book_viesws.BookDeleteView.as_view(), name="book_delete"),
]