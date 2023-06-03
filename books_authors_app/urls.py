from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('createBook', views.createBook),
    path('bookOne', views.bookOne),
    path('addAuthorOne', views. addAuthorOne),
    path('addAuthorTwo', views. addAuthorTwo),
    path('addAuthorThree', views. addAuthorThree),
    path('addAuthorFour', views. addAuthorFour),
    path('addAuthorFive', views. addAuthorFive),
    path('bookTwo', views.bookTwo),
    path('bookThree', views.bookThree),
    path('bookFour', views.bookFour),
    path('bookFive', views.bookFive),
    path('authors', views.authors),
    path('createAuthor', views.createAuthor),
    path('authorOne', views.authorOne),
    path('authorTwo', views.authorTwo),
    path('authorThree', views.authorThree),
    path('authorFour', views.authorFour),
    path('addBook', views.addBookOne),
    path('addBook', views.addBookTwo),
    path('addBook', views.addBookThree),
    path('addBook', views.addBookFour),
]