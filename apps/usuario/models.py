from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def _create_user(self,  username, email, nombres, apellidos, password, is_staff, is_superuser, **extra_fields):
        '''esta función va a ser llamada cuando utilicemos la consola '''
        user = self.model(  # acá solo hemos nstanciado un objeto usuario
            username=username,
            email=self.normalize_email(email),
            nombres=nombres,
            apellidos=apellidos,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
            )
        user.set_password(password)
        user.save(using=self.db)  # using=self.db --> le decimos a django que use la base de datos actual
        
        return  user
    
    def create_user(self,  username, email, nombres, apellidos, password=None, **extra_fields):
        '''función para crear a un usuario'''
        return self._create_user(username, email, nombres, apellidos, password, False, False, **extra_fields)
        
    def create_user(self,  username, email, nombres, apellidos, password=None, **extra_fields):
        '''función para crear a un super usuario'''
        return self._create_user(username, email, nombres, apellidos, password, True, True, **extra_fields)
        
    # def create_user(self,  username, email, nombres, apellidos, password=None):
    #     if not email:
    #         raise ValueError("el usuario debe tener un correo electrónico")
        
    #     usuario = self.model(  # acá solo hemos nstanciado un objeto usuario
    #         username=username,
    #         email=self.normalize_email(email),
    #         nombres=nombres,
    #         apellidos=apellidos
    #         )
    #     return usuario
        
    #     usuario.set_password(password)  ## encripta la contraseña 
    #     usuario.save()
        
    # def create_superuser(self,  username,email, nombres, apellidos, password=None):
    #     usuario = self.create_user(
    #         username,
    #         email,
    #         nombres,
    #         apellidos,
    #         password=password
    #         )
    #     usuario.usuario_administrador=True
    #     usuario.save()
    #     return usuario
        
        


class Usuario(AbstractBaseUser, PermissionsMixin): 
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, max_length=254)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    imagen = models.ImageField( upload_to='perfil/', max_length=100, blank=True, null=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador  = models.BooleanField(default=False) # Para identificar que usuarios pueden entrar al admin de django 
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects=UsuarioManager() # enlazando el modelo con el manager
    
    USERNAME_FIELD = 'username' # Hace referencia a cual será el campo por el cual se logeará el usuario
    
    REQUIRED_FIELDS = ['nombres','apellidos','email'] # campos requeridos, campos que serán pedidos por consola
    
    def __str__(self):
        return f'Usuario {self.nombres}, {self.apellidos}'
    
    ##debemos definirle los permisos
    # def has_perm(self, perm, obj=None):
    
    #     return True
    # def has_module_perms(self, app_label):
    #     return True
    
    # @property
    # def is_staff(self):  
    #     '''método que retorna si el usuario es administrador o no '''
    #     return self.usuario_administrador
    
    ### están comentariados poruqe ya no son necesarios, PermisosMixin los define de forma automática 
