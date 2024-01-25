from django.urls import path
from . import views

urlpatterns = [
    path('', views.fizzbuzz_view, name='index')
]