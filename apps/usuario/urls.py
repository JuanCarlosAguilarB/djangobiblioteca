from django.urls import path,include
from django.contrib.auth.decorators import login_required

from apps.usuario import views

urlpatterns = [
    path('listar_usuarios/', views.ListarUsuarios.as_view(),name='listar_usuarios'),
    path('borrar_usuario/<int:pk>/', views.BorrarUsuario.as_view(),name='borrar_usuarios'),
    path('editar_usuarios/<int:pk>/', views.ActualizarUsuario.as_view(),name='editar_usuarios'),
    path('crear_usuarios/', views.CrearUsuario.as_view(),name='crear_usuarios'),
]

