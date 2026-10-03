from django.urls import path
from amazon import views

urlpatterns = [
    path("", views.home, name="home"),
]