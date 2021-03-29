from django.db import models
from stdimage.models import StdImageField

class Base(models.Model):
    create = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Updated', auto_now=True)
    active = models.BooleanField('active?', default=True)

    class Meta:
        abstract = True

class Service(Base):
    ICONS_CHOICE = (
        ('lni-cog', 'Gear'),
        ('lni-stats-up', 'Grafic'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket'),
    )
    service = models.CharField('Services', max_length=100)
    description = models.TextField('Description', max_length=200)
    icons = models.CharField('Icons', max_length=12, choices=ICONS_CHOICE)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service