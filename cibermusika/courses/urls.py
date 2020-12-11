from django.urls import path
from .views import CoursesView

urlpatterns = [
    path('', CoursesView.as_view(), name="courses"),
    ]