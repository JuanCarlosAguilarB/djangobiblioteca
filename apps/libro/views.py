from django.shortcuts import render,redirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic
from django.urls import reverse_lazy

from .forms import AutorForm
from libro.models import Autor
from libro import models


class Home(generic.TemplateView):
    template_name = 'index.html'
    
class ListadoAutores(generic.TemplateView):
    model = models.Autor
    template_name = 'libro/listar_autor.html'
    print(models.Autor.objects.all()[0].estado)
    queryset = models.Autor.objects.filter(estado=True)
    print(queryset)
    # context_object_name = 'autores'  ## definir cómo se hace 
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['autores'] = self.queryset
        return context

class UpdateAutoresView(generic.UpdateView):
    '''view para actualizar autores'''
    model = models.Autor
    template_name = 'libro/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor')
    
class CreateAutor(generic.CreateView):
    '''view para crear autores'''
    model = models.Autor
    template_name = 'libro/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor')
    
class DeleteAutor(generic.DeleteView):
    model = models.Autor
    # success_url = 'libro/listar_autor.html'
    
    def post(self, request,pk,*args, **kwargs):
        object = models.Autor.objects.get(pk=pk)
        object.estado = False
        object.save()
        return redirect('libro:listar_autor')
        


def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('home')
    else:
        autor_form = AutorForm()
    return render(request,'libro/crear_autor.html',{'autor_form':autor_form})


def listarAutor(request):
    autores = models.Autor.objects.filter(estado = True)
    
    
    return render(request,'libro/listar_autor.html',{'autores':autores})

def editarAutor(request,id):
    autor_form = None
    error = None
    try:
        autor = Autor.objects.get(id = id)
        if request.method == 'GET':
            autor_form = AutorForm(instance = autor)
        else:
            autor_form = AutorForm(request.POST, instance = autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect(('libro:listar_autor'))
    except ObjectDoesNotExist as e:
        error = e
    return render(request,'libro/crear_autor.html',{'autor_form':autor_form,'error':error})

def eliminarAutor(request,id):
    autor = Autor.objects.get(id = id)
    autor.estado = False
    autor.save()
    return redirect('libro:listar_autor')
