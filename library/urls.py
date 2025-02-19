from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='detail'),
]