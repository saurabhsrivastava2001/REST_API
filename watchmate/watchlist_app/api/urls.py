from django.urls import path, include

from . import views

urlpatterns = [
    path('list/', views.movie_list, name='movie-list'),  # Endpoint for listing
    path('<int:pk>/', views.movie_detail, name='movie-detail'),  # Endpoint for detail view
]
