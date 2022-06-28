from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('addContact/', views.addContact, name="addContact"),
    path('deleteContact/<str:pk>/', views.deleteContact, name="deleteContact"),
    path('editContact/<str:pk>/', views.editContact, name="editContact")
]