from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Usuario

class FormsLogin(AuthenticationForm):
    def __inif__(self,*args, **kwargs):
        super(FormsLogin,self).__init__(*args, **kwargs)
        self.field['username'].widget.attrs['class'] = 'form-control'
        self.field['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.field['password'].widget.attrs['class'] = 'form-control'
        self.field['password'].widget.attrs['placeholder'] = 'contraseña'
        
class FormUsuario(forms.ModelForm):
    '''Formulario de regstro de un usuario en la base de datos
    
    variables
        password1 contraseña
        password2 verificación de la contraseña 
    '''
    
    ## estamos definiendo campos adicionales
    
    password1 = forms.CharField(label='contraseña',widget=forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder': 'Ingrese su contraseña',
            'id': 'password1',
            'required':'required'
        }
        
    ))
    
    password2 = forms.CharField(label='contraseña de conrifmación',widget=forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder': 'Ingrese su contraseña',
            'id': 'password2',
            'required':'required'
        }
        
    ))
    
    class Meta:
        model = Usuario
        fields = '__all__'
        