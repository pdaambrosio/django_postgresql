import uuid
from django.db import models
from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

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

class Position(Base):
    position = models.CharField('Position', max_length=100)

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

    def __str__(self):
        return self.position

class Team(Base):
    name = models.CharField('Name', max_length=100)
    position = models.ForeignKey('core.Position', verbose_name='Position', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    image = StdImageField('Image', upload_to=get_file_path, variations={'thumb':{'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name