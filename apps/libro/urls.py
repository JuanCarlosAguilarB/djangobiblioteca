from django.urls import path
from .views import crearAutor,listarAutor,editarAutor,eliminarAutor, Home
from libro import views

urlpatterns = [
    path('listar_autor/',views.ListadoAutores.as_view(), name = 'listar_autor'),
    path('crear_autor/',views.CreateAutor.as_view(), name = 'crear_autor'),
    path('listar_autor/',listarAutor, name = 'listar_autor'),
    path('editar_autor/<int:pk>',views.UpdateAutoresView.as_view(), name = 'editar_autor'),
    path('eliminar_autor/<int:pk>',views.DeleteAutor.as_view() , name = 'eliminar_autor')
]

