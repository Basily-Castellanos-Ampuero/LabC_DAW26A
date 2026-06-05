from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_destinos, name='lista_destinos'),
    path('agregar/', views.agregar_destino, name='agregar_destino'),
    path('modificar/<int:pk>/', views.modificar_destino, name='modificar_destino'),
    path('eliminar/<int:pk>/', views.eliminar_destino, name='eliminar_destino'),
]
