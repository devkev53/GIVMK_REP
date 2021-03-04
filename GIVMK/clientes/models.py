from django.db import models

# Create your models here.
GENDER_CHOICES = [
    ('_Male', 'M'),
    ('_Female', 'F'),

]

class Cliente(models.Model):
    firts_name = models.CharField('_name', max_length=75)
    last_name = models.CharField('_last_name', max_length=75, blank=True, null=True)
    gender = models.CharField('_gender', max_length=1, choices=GENDER_CHOICES)
