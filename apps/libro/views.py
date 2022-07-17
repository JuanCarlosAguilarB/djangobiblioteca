from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic

from .forms import AutorForm
from libro.models import Autor


class Home(generic.TemplateView):
    template_name = 'index.html'
    
class ListadoAutores(generic.TemplateView):
    model = Autor
    template_name = 'libro/listar_autor.html'
    queryset = Autor.objects.filter(estado=True)
    # context_object_name = 'autores'  ## definir cómo se hace 
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['autores'] = self.queryset
        return context


def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')
    else:
        autor_form = AutorForm()
    return render(request,'libro/crear_autor.html',{'autor_form':autor_form})


def listarAutor(request):
    autores = Autor.objects.filter(estado = True)
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
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e
    return render(request,'libro/crear_autor.html',{'autor_form':autor_form,'error':error})

def eliminarAutor(request,id):
    autor = Autor.objects.get(id = id)
    autor.estado = False
    autor.save()
    return redirect('libro:listar_autor')
