from django.contrib.auth.models import AbstractUser
from django.db import models

from GIVMK.settings import MEDIA_URL, STATIC_URL
from django.contrib.auth.models import User
from GIVMK.settings import AUTH_USER_MODEL
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.utils.translation import gettext_lazy as _

# Create your models here.


def custom_upload_to(instance, filename):
    '''Este metodo elimina de nuestra base de datos una imagen
    de una instancia se esta ya tenia una imagen previa'''
    # Obtiene la imagen antigua de la instancia en cuestion
    old_instance = User.objects.get(pk=instance.pk)
    # Borra la imagen de la que se ha seleccionado
    old_instance.foto.delete()
    return 'Users/%Y/%m/%d' + filename


class User(AbstractUser):
    img = models.ImageField(
        upload_to='Users/%Y/%m/%d', null=True, blank=True, verbose_name='Avatar')
    userCreate = models.ForeignKey(
        AUTH_USER_MODEL, verbose_name=_('Creator User'), on_delete=models.PROTECT,
        related_name='userCreate%(app_label)s_%(class)s_related', blank=True, null=True)
    dateCreate = models.DateField(_('Creation date'), auto_now_add=True, blank=True, null=True)
    userUpdate = models.ForeignKey(
        AUTH_USER_MODEL, verbose_name=_('Modifier User'), on_delete=models.PROTECT,
        related_name='userUpdate%(app_label)s_%(class)s_related', blank=True, null=True)
    dateUpdate = models.DateField(_('Modification Date'), auto_now=True, blank=True, null=True)

    # campo que creara la imagen en thubnail
    img_thubmnail = ImageSpecField(
        source='img',
        processors=[ResizeToFill(100, 100)],
        format='JPEG',
        options={'quality': 100})

    def get_img(self):
        if self.img_thubmnail:
            return '{}{}'.format(MEDIA_URL, self.img_thubmnail)
        return '{}{}'.format(STATIC_URL, 'core/img/image-not.jpg')