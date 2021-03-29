from django.db import models
from stdimage.models import StdImageField

class Base(models.Model):
    create = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Updated', auto_now=True)
    active = models.BooleanField('active?', default=True)

    class Meta:
        abstract = True