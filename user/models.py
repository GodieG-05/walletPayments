from django.db import models
from django.contrib.auth.models import AbstractUser # Para dotar a mi clase User de los atributos user de django y los nuestros
from django.utils.translation import gettext_lazy as _
class User(AbstractUser): # ES UNA BUENA PRACTICA EMPEZAR LA APP HACIENDO UN OVERRIDE DEL USUARIO DE DJANGO PARA EN UN FUTURO AMPLIAR SU FUNCIONALIDAD
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=False, blank=True)
    # wallet =
    id_user_stripe = models.CharField(max_length=255, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []