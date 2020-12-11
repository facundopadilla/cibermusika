from django.urls import path
from .views import SearchView, FilterView

urlpatterns = [
    path('<str:cancion>/', FilterView.as_view(), name="filterview"),
    path('', SearchView.as_view(), name="search"),
    ]