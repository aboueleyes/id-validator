from django.urls import path, include
from . import views


urlpatterns: list = [
    path('<str:id>', views.index, name='index'),
]
