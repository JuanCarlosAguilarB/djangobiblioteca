from django import forms
from libro.models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
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
