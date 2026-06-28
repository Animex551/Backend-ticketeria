from django.db import models
# Importaciones necesarias para que funcione como AUTH_USER_MODEL
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UsuariosManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)  # Encripta la contraseña de forma segura
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_IT', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)


class Usuarios(AbstractBaseUser, PermissionsMixin):
    # Al usar primary_key=True, Django no creará el ID autoincremental para esta tabla
    email = models.CharField(max_length=255, primary_key=True)
    username = models.CharField(max_length=255)
    
    # NOTA: El campo 'password' ya lo incluye AbstractBaseUser de forma nativa y encriptada, 
    # por lo que no es necesario declararlo aquí manualmente como antes.
    
    is_IT = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    # Campos obligatorios internos que requiere Django Admin y la gestión de sesiones
    is_staff = models.BooleanField(default=False)  # Permite acceso al panel de administración
    is_active = models.BooleanField(default=True)  # Permite saber si el usuario está activo

    # Configuración de los campos de autenticación obligatorios
    USERNAME_FIELD = 'email'       # Indica que el inicio de sesión se hace con el correo
    REQUIRED_FIELDS = ['username'] # Campos requeridos en la terminal al usar createsuperuser

    objects = UsuariosManager()    # Enlaza el gestor personalizado de arriba

    def __str__(self):
        return self.username


class Zonas(models.Model):
    # Django crea el campo 'id' (integer, primary key) automáticamente
    sucursal = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.sucursal} - {self.sector}"


class TipoFalla(models.Model):
    tipo = models.CharField(max_length=255)
    prioridad = models.IntegerField()

    def __str__(self):
        return self.tipo


class Tickets(models.Model):
    nombre = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    
    # Llaves foráneas
    id_cliente = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='tickets_cliente')
    id_tecnico = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True, blank=True, related_name='tickets_asignados')
    id_zona_problema = models.ForeignKey(Zonas, on_delete=models.CASCADE)
    id_falla = models.ForeignKey(TipoFalla, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ticket #{self.id}: {self.nombre}"


class Adjunto(models.Model):
    path = models.CharField(max_length=255)
    id_tickets = models.ForeignKey(Tickets, on_delete=models.CASCADE, related_name='adjuntos')

    def __str__(self):
        return f"Adjunto {self.id} de Ticket {self.id_tickets_id}"


class BitacoraTicket(models.Model):
    id_ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE, related_name='bitacoras')
    tecnico_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='bitacoras_escritas')
    commit = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bitácora {self.id} - Ticket {self.id_ticket_id}"


class BitacoraAdjuntos(models.Model):
    path = models.CharField(max_length=255)
    id_bitacora = models.ForeignKey(BitacoraTicket, on_delete=models.CASCADE, related_name='adjuntos_bitacora')

    def __str__(self):
        return f"Adjunto {self.id} de Bitácora {self.id_bitacora_id}"