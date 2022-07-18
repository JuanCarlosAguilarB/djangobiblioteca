from django import forms
from libro import models


class AutorForm(forms.ModelForm):
    class Meta:
        model = models.Autor
        fields = ['nombre','apellidos','nacionalidad','descripcion']
        labels = {
            'nombre':  'Nombre del autor',
            'apellidos':'Apellidos del autor',
            'nacionalidad': 'Nacionalidad del autor',
            'descripcion':'descripción'
            
        }
        ## definición de los campos html en la plantilla 
        widgets = {
            'nombre': forms.TextInput(attrs = {'class': 'form-control','placeholder': labels['nombre'],'id':'nombre'}),
            'apellidos': forms.TextInput(attrs = {'class': 'form-control','placeholder': labels['apellidos'],'id':'apellidos'}),
            'nacionalidad': forms.TextInput(attrs = {'class': 'form-control','placeholder': labels['nacionalidad'],'id':'nacionalidad'}),
            'descripcion': forms.Textarea(attrs = {'class': 'form-control','placeholder': labels['descripcion'],'id':'descripcion'})
        }

class LibroFroms(forms.ModelForm):
    class Meta:
        model = models.Libro
        fields = ['titulo','fecha_publicacion','autor_id']
        labels = {
            'titulo':  'Título del libro',
            'fecha_publicacion':'fecha de publicación del libro',
            'autor_id': 'Id del autor'          
            
        }
        ## definición de los campos html en la plantilla 
        widgets = {
            'titulo': forms.TextInput(attrs = {'class': 'form-control','placeholder': labels['titulo'],'id':'titulo'}),
            'fecha_publicacion': forms.SelectDateWidget(attrs = {'class': 'form-control'}),# (attrs = {'class': 'form-control','placeholder': labels['fecha_publicacion'],'id':'fecha_publicacion'}),
            'autor_id': forms.SelectMultiple(attrs = {'class': 'form-control','id':'autor_id'}),
            
        }