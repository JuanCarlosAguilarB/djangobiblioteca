from django.urls import path
from django.contrib.auth.decorators import login_required

from libro import views

urlpatterns = [
    path('listar_autor/',login_required(views.ListadoAutores.as_view()), name = 'listar_autor'),
    path('crear_autor/',views.CreateAutor.as_view(), name = 'crear_autor'),
    path('editar_autor/<int:pk>',views.UpdateAutoresView.as_view(), name = 'editar_autor'),
    path('eliminar_autor/<int:pk>',views.DeleteAutor.as_view() , name = 'eliminar_autor'),
    
    path('listar_libro/',views.ListarLibros.as_view() , name = 'listar_libros'),
    path('crear_libro/',views.CrearLibro.as_view(), name = 'crear_libro'),    
    path('editar_libro/<int:pk>/',views.UpdateLibroView.as_view(), name = 'editar_libro'),    
    path('eliminar_libro/<int:pk>/',views.EliminarLibro.as_view(), name = 'eliminar_libro'),    
]

