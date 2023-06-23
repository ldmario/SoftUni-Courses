from django.urls import path
from library.library_books import views

urlpatterns = [
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:pk>', views.edit_book, name='edit_book'),
    path('details/<int:pk>', views.details_book, name='details_book'),
]
