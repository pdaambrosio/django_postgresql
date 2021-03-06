# Generated by Django 3.1.7 on 2021-04-04 22:19

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='active?')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
            ],
            options={
                'verbose_name': 'Position',
                'verbose_name_plural': 'Positions',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='active?')),
                ('service', models.CharField(max_length=100, verbose_name='Services')),
                ('description', models.TextField(max_length=200, verbose_name='Description')),
                ('icons', models.CharField(choices=[('lni-cog', 'Gear'), ('lni-stats-up', 'Grafic'), ('lni-users', 'Users'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Rocket')], max_length=12, verbose_name='Icons')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='active?')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('bio', models.TextField(max_length=200, verbose_name='Bio')),
                ('image', stdimage.models.StdImageField(upload_to='team', verbose_name='Image')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.position', verbose_name='Position')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
    ]
