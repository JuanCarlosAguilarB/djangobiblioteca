from django.urls import path
from .views import crearAutor,listarAutor,editarAutor,eliminarAutor, Home
from libro import views

urlpatterns = [
    path('listar_autor/',views.ListadoAutores.as_view(), name = 'listar_autor'),
    path('crear_autor/',crearAutor, name = 'crear_autor'),
    path('listar_autor/',listarAutor, name = 'listar_autor'),
    path('editar_autor/<int:pk>',views.UpdateAutoresView.as_view(), name = 'editar_autor'),
    path('eliminar_autor/<int:id>',eliminarAutor, name = 'eliminar_autor')
]

