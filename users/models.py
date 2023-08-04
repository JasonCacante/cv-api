"""Modelo de Usuarios"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    """Clase de Usuario"""
    ID_TYPE = [
        ('Registro Civil', 'Registro Civil'),
        ('Tarjeta de Identidad', 'Tarjeta de Identidad'),
        ('Cédula de Ciudadanía', 'Cédula de Ciudadanía'),
        ('Cédula de Extranjería', 'Cédula de Extranjería'),
        ('Pasaporte', 'Pasaporte'),
        ('Permiso Temporal', 'Permiso Temporal'),
    ]

    email = models.EmailField(verbose_name="Correo Electrónico", unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    id_type = models.CharField(
        verbose_name="Tipo de Identificación",
        max_length=50,
        choices=ID_TYPE
    )
    identificaction = models.CharField(
        verbose_name="Número de Identificación",
        max_length=50
    )
    photo = models.ImageField(
        verbose_name="Foto de Perfil",
        upload_to='img/usuarios',
    )
    country = models.BooleanField(
        verbose_name="País de Residencia",
        max_length=150
    )
    city = models.BooleanField(
        verbose_name="Ciudad de Residencia",
        max_length=150
    )
    address = models.TextField(verbose_name="Dirección De Residencia")
    birtdhday = models.DateField(
        verbose_name="Fecha de Nacimiento",
        null=True,
        blank=True
    )
    phone = models.CharField(
        verbose_name="Número de Teléfono",
        max_length=20,
        null=True,
        blank=True
    )
    relocate = models.BooleanField(
        "Disponibilidad para reubicarse",
        default=False
    )
    occupation = models.CharField(verbose_name="Ocupación", max_length=150)
    is_recruter = models.BooleanField("Reclutador", default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.email)


class Links(models.Model):
    """Clase de Links"""
    LINK_TYPE = [
        ('Linkedin', 'Linkedin'),
        ('Repositorio', 'Repositorio'),
        ('WebSite', 'WebSite'),
        ('RedSocial', 'RedSocial'),
        ('GitLab', 'GitLab'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_link = models.CharField(
        verbose_name="Tipo de Link",
        max_length=50,
        choices=LINK_TYPE
    )
    link_url = models.URLField(verbose_name="Link")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class"""
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"

    def __str__(self):
        return str(self.link_url)


class ResumeUser(models.Model):
    """Clase de Resumen de Usuario"""
    RESUME_SECTION = [
        ('PP', 'Perfil Profesional'),
        ('RR', 'Resumen Profesional'),
        ('RF', 'Resume Hechos'),
        ('RS', 'Resumen Sumario'),
        ('RA', 'Resumen Adjetivos'),
        ('RC', 'Resumen Contacto'),
    ]

    type_resume = models.CharField(
        verbose_name="Tipo de Resumen",
        max_length=50,
        choices=RESUME_SECTION
    )
    resumes = RichTextField(verbose_name="Resumen")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class"""
        verbose_name = "Resumen"
        verbose_name_plural = "Resumenes"

    def __str__(self):
        return str(self.type_resume)
