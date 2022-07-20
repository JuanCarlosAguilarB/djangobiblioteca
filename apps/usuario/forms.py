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
        
    def clean_password2(self):
        '''este método es para validar el campo password2 en el formulario, ya que este no está incluido en el modelo
        
            Valida que ambas contraseñas ingresadas sean iguales antes de ser encriptadas y guardadas en la base de datos
            
            excepciones:
            -ValidationError   -- ambas contraseñas no son iguales 
        '''
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
            # cleaned_data --> es un diccionario de todos los campos del formulario que ya han sido validados
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        
        return password2 # ---> retornamso password 2 para que el flujo de trabajo no se interrumpa 
                        ## retornamos esta variable, porque este valor se va a asignar a la variable que 
                        # #tenga el nombre del método en cuestion, o del campo por el cual se está validando
        
    def save(self, commit=True): ## commit indica que se continua con el registro
        '''redefinimos el método save para poder guardar las contraseñas '''
        
        # el parámetro en commit=True es debido a que se quiere proseguir con el flufo normal del trabajo
            # es decir, invocar al método save del modelo y guardarlo en la base de datos 
            # cuando lo cambiamos False en el método de la clase padre, estamos indicando qeu guardamos la instancia
            # en la variable user, no en la base de datos
            # esto lo hacemos para poder encriptar las contraseñas 
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
        return user
        
        