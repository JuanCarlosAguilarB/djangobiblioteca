from django.shortcuts import render,redirect, reverse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache  # para que no se almacene en cache 
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout ## para indicarle a django que inicie una seción 
from django.http import HttpResponseRedirect
from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from usuario import forms, models, mixins

from django.views import generic
class Home(mixins.LoginSuperUsuarioMixin,generic.TemplateView):
    template_name = 'index.html'




class Login(FormView):
    template_name = 'login.html'
    form_class = forms.FormsLogin
    success_url = reverse_lazy('home')
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form): # este método se encarga de validar el fómulario que se utiliza en esta vista
        # este método se ejecuta antes de llamar al métoodo post
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

#logout es simplemente una función que recive una petición y va a cerrar la petición que encuentre en esta petición 

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
    
        

    
class CrearUsuario(generic.CreateView):
    model = models.Usuario
    form_class = forms.FormUsuario
    template_name = 'usuario/crear_usuario.html'
    success_url = reverse_lazy('usuarios:listar_usuarios')
    
    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST) ## estamos reciviendo toda la información que viene de la petición 
        
        if form.is_valid():
            '''Se va a registrar el form en la base de datos directamente'''
            nuevo_usuario = models.Usuario(
                email = form.cleaned_data['email'],
                username = form.cleaned_data.get('username'), #tambien podemos acceder por medio de get
                nombres = form.cleaned_data.get('nombres'),
                apellidos=form.cleaned_data['apellidos']
            )
            nuevo_usuario.set_password(form.cleaned_data.get('password1'))
            nuevo_usuario.save()  ###  estamos usando el método save del modelo
            
            return redirect('usuarios:listar_usuarios')
        else:
            return render(request, self.template_name,{'form':form})
        
        ## si en algún momento mandaramos a llamar el método save del fórmulario, encriptariamos la contaraseña 2 veces 
        
        
        
        
    
class ListarUsuarios(PermissionRequiredMixin ,generic.ListView): ## PermissionRequiredMixin solicita verificar los permisos que le indiquemos 
    permission_required = 'usuario.view_usuario'
    model = models.Usuario
    template_name = 'usuario/listar_usuarios.html'
    queryset = models.Usuario.objects.filter(usuario_activo=True)
    context_object_name = 'usuario'

class BorrarUsuario(generic.DeleteView):
    model = models.Usuario
    
    def post(self, request, pk, *args, **kwargs):
        object = models.Usuario.objects.get(pk=pk)
        object.usuario_activo=False
        object.save()
        return redirect('usuarios:listar_usuarios') 
    
class ActualizarUsuario(generic.UpdateView):
    model = models.Usuario
    form_class = forms.FormUsuario
    template_name = 'usuario/crear_usuario.html'
    success_url = reverse_lazy('usuarios:listar_usuarios')