from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, nombres, apellidos, password=None):
        if not email:
            raise ValueError("el usuario debe tener un correo electrónico")
        
        usuario = self.model(  # acá solo hemos nstanciado un objeto usuario
            username=username,
            email=self.normalize_email(email),
            nombres=nombres,
            apellidos=apellidos
            )
        
        usuario.set_password(password)  ## encripta la contraseña 
        usuario.save()
        
    def create_superuser(self, email, username, nombres, apellidos, password=None):
        usuario = self.create_user(
            username,
            email,
            nombres,
            apellidos
            )
        usuario.usuario_administrador=True
        usuario.save()
        


class Usuario(AbstractBaseUser): 
    username = models.CharField( max_length=100, unique=True)
    email = models.EmailField(unique=True, max_length=254)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    imagen = models.ImageField( upload_to='perfil/', max_length=100, blank=True, null=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador  = models.BooleanField(default=False) # Para identificar que usuarios pueden entrar al admin de django 
    
    objects=UsuarioManager # enlazando el modelo con el manager
    
    USERNAME_FIELD = 'username' # Hace referencia a cual será el campo por el cual se logeará el usuario
    REQUIRED_FIELDS = ['email','nombres','apellidos'] # campos requeridos, campos que serán pedidos por consola
    
    def __str__(self):
        return f'Usuario {self.nombres}, {self.apellidos}'
    
    ##debemos definirle los permisos
    def has_perm(self, perm, object=None):
        return True
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador
    

