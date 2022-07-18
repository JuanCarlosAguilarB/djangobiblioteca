from django.shortcuts import render,redirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic
from django.urls import reverse_lazy

from .forms import AutorForm
from libro.models import Autor
from libro import models, forms


class Home(generic.TemplateView):
    template_name = 'index.html'
    
class ListadoAutores(generic.TemplateView):
    model = models.Autor
    template_name = 'libro/listar_autor.html'
    queryset = models.Autor.objects.filter(estado=True)
    # context_object_name = 'autores'  ##  lo entrega como un object_list
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
        
class ListarLibros(generic.View):
    model = models.Libro
    template_name = 'libro/libro/libro_list.html'    
    form_class = forms.LibroFroms
    context_object_name = 'libro'  
    def get_queryset(self):
        return models.Libro.objects.filter(estado=True)
    
    def get(self,request,*args, **kwargs):   
        return render(request, self.template_name, self.get_context_data())
    
    def get_context_data(self, **kwargs):
        context = {}
        context['libro'] = self.get_queryset()
        context['form'] = self.form_class 
        return context
    
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro:listar_libros')
        

class CrearLibro(generic.CreateView):
    model = models.Libro
    template_name = 'libro/libro/crear_libro.html'
    form_class = forms.LibroFroms
    success_url = reverse_lazy('libro:listar_libros')
    
class UpdateLibroView(generic.UpdateView):
    '''view para actualizar libro'''
    model = models.Libro
    template_name = 'libro/libro/libro_list.html'
    form_class = forms.LibroFroms
    success_url = reverse_lazy('libro:listar_libros')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["libro"] = models.Libro.objects.filter(estado=True)
        return context
    
    
class EliminarLibro(generic.DeleteView):
    model = models.Libro
    
    def post(self, request,pk,*args, **kwargs):
        object = models.Libro.objects.get(pk=pk)
        object.estado = False
        object.save()
        return redirect('libro:listar_libros')
        