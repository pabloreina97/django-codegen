from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """
        Crea y devuelve un usuario con el email y la contraseña proporcionadas.
        """
        if not email:
            raise ValueError(_("Se debe proporcionar un email"))
        if not password:
            raise ValueError(_("Se debe proporcionar una contraseña"))
        if 'role' not in extra_fields:
            raise ValueError(_("Se debe proporcionar un rol"))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        """
        Crea y devuelve un superusuario con correo electrónico y contraseña.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        # Aquí estableces el rol de administrador
        extra_fields.setdefault('role', MANAGER)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('El superusuario debe tener is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                _('El superusuario debe tener is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    verification_deadline = models.DateTimeField(
        default=timezone.now() + timedelta(days=7))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
