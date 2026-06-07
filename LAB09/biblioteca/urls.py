from django.urls import path
from . import views

urlpatterns = [
    # Inicio
    path('', views.inicio, name='inicio'),

    # Autores
    path('autores/', views.autor_lista, name='autor_lista'),
    path('autores/nuevo/', views.autor_nuevo, name='autor_nuevo'),
    path('autores/<int:pk>/editar/', views.autor_editar, name='autor_editar'),
    path('autores/<int:pk>/eliminar/', views.autor_eliminar, name='autor_eliminar'),
    path('autores/<int:pk>/', views.autor_detalle, name='autor_detalle'),

    # Géneros
    path('generos/', views.genero_lista, name='genero_lista'),
    path('generos/nuevo/', views.genero_nuevo, name='genero_nuevo'),
    path('generos/<int:pk>/eliminar/', views.genero_eliminar, name='genero_eliminar'),

    # Libros
    path('libros/', views.libro_lista, name='libro_lista'),
    path('libros/nuevo/', views.libro_nuevo, name='libro_nuevo'),
    path('libros/<int:pk>/editar/', views.libro_editar, name='libro_editar'),
    path('libros/<int:pk>/eliminar/', views.libro_eliminar, name='libro_eliminar'),

    # PDF y Email
    path('pdf/', views.generar_pdf, name='generar_pdf'),
    path('email/', views.enviar_email, name='enviar_email'),
]
