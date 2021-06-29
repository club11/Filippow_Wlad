from django.urls import path
from django.conf.urls.static import static
from books import views as books_book_viesws

app_name = 'books'

urlpatterns = [
    path('home/', books_book_viesws.HomeListView.as_view(), name="home"),

    #path('books/', books_book_viesws.BookListView.as_view(), name="books"),
    path('book_list/', books_book_viesws.BookListView.as_view(), name="book_list"),
    path('book_detail/<int:pk>/', books_book_viesws.BookDetailView.as_view(), name="book_detail"),
    path('book_create/', books_book_viesws.BookCreateView.as_view(), name="book_create"),
    path('book_update/<int:pk>/', books_book_viesws.BookUpdateView.as_view(), name="book_update"),
    path('book_delete/<int:pk>/', books_book_viesws.BookDeleteViiew.as_view(), name="book_delete"),

    path('home_customer/', books_book_viesws.HomeListViewCustomer.as_view(), name="home_customer"),
    path('book_list_customer/', books_book_viesws.BookListCustomerView.as_view(), name="book_list_customer"),
    path('book_detail_customer/<int:pk>/', books_book_viesws.BookDetailCustomerView.as_view(), name="book_detail_customer"),

]