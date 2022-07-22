from django.shortcuts import render,redirect, reverse
from django.urls import reverse_lazy
from django.contrib import messages

class LoginSuperUsuarioMixin(object):
    '''Esta clase verifica que el usuario esté logueado y sea un supe usuario'''
    
    def dispatch(self, request, *args, **kwargs):  ## llamamos a dispatch porque esta ee el método que se llama en todas las vistas basadas en clases para verificar que método http se está usando 
        if request.user.is_authenticated:
            if request.user.is_staff:
                return super().dispatch(request, *args, **kwargs)
            
        return redirect('home')

class ValidarPermisosRequeridosMixin(object):
    permission_required = ''        ## indicamos los permisos que queremos validar 
    url_redirect = None             ## es la ruta a la cual queremos redirigir al usuario
    
    def get_perms(self):
        if isinstanc(self.permission_required, str):
            return  (self.permission_required)
        else:
            return  self.permission_required
    
    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('login')
        return self.url_redirect
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):
            '''estamos preguntando si tiene los permisos y si los tiene continua la ejecución'''
            return super().dispatch(request,*args, **kwargs)
        messages.error(request, 'No tiense permisos para realizar esta acción')
        return redirect(self.get_url_redirect())
    