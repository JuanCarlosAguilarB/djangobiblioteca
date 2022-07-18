from django.contrib.auth.forms import AuthenticationForm

class FormsLogin(AuthenticationForm):
    def __inif__(self,*args, **kwargs):
        super(FormsLogin,self).__init__(*args, **kwargs)
        self.field['username'].widget.attrs['class'] = 'form-control'
        self.field['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.field['password'].widget.attrs['class'] = 'form-control'
        self.field['password'].widget.attrs['placeholder'] = 'contraseña'
        
        