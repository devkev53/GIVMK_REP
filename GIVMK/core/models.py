from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from GIVMK.settings import AUTH_USER_MODEL
from datetime import date
from crum import get_current_user


# Create your models here.
GENDER_CHOICES = [
    ('M', _('Male')),
    ('F', _('Female')),
]

class Base(models.Model):
    userCreate = models.ForeignKey(
        AUTH_USER_MODEL, verbose_name=_('Creator User'), on_delete=models.PROTECT,
        related_name='userCreate%(app_label)s_%(class)s_related', blank=True, null=True)
    dateCreate = models.DateField(_('Creation date'), auto_now_add=True, blank=True, null=True)
    userUpdate = models.ForeignKey(
        AUTH_USER_MODEL, verbose_name=_('Modifier User'), on_delete=models.PROTECT,
        related_name='userUpdate%(app_label)s_%(class)s_related', blank=True, null=True)
    dateUpdate = models.DateField(_('Modification Date'), auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = "Base"
        verbose_name_plural = "Bases"

    def __str__(self):
        pass

    def save(self):
        print('Se creo un nuevo producto')
        # self.calcularExistencia()
        # Guardando el user
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.userCreate = user
            else:
                self.userUpdate = user
        super(Base, self).save()

class BasePhone(Base):
    phone_number = models.CharField(_('Phone Number'), max_length=15, help_text=_('Add a phone number'))
    is_favorite = models.BooleanField(_('Favorite'), help_text=_('Check only is favorite'), default=True)

    class Meta:
        abstract = True
        verbose_name = _('Phone')
        verbose_name_plural = _('Phones')

    def __str__(self):
        return self.phone_number

class BasePerson(Base):
    firts_name = models.CharField(_('first_name'), max_length=75)
    last_name = models.CharField(_('last_name'), max_length=75, blank=True, null=True)
    gender = models.CharField(_('gender'), max_length=1, choices=GENDER_CHOICES)
    idNumber = models.CharField(_('Id Number'), max_length=75, blank=True, null=True)
    nacimiento = models.DateField('Fecha de Nacimiento', blank=True, null=True)
    tel = models.CharField(_('Phone'), max_length=75, blank=True, null=True)

    def edad(self):
        hoy = date.today()
        fechanacimiento=self.nacimiento
        edad = hoy.year - fechanacimiento.year - ((hoy.month, hoy.day) < (fechanacimiento.month, fechanacimiento.day))
        #primero restamos los años y luego restamos la comparación entre mes y día actual y mes y día de nacimiento.
        return edad

    class Meta:
        abstract = True
        verbose_name = _('BasePerson')
        verbose_name_plural = _('BasePersons')

    def __str__(self):
        return '%s %s' % (self.firts_name, self.last_name)
