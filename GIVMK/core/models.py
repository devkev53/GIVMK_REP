from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Phone(models.Model):
    phone_number = models.CharField(_('Phone Number'), max_length=15, help_text=_('Add a phone number'))
    is_favorite = models.BooleanField(_('Favorite'), help_text=_('Check only is favorite'))

    class Meta:
        verbose_name = _('Phone')
        verbose_name_plural = _('Phones')

    def __str__(self):
        return self.phone_number
