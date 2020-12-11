# Generated by Django 3.1.4 on 2020-12-11 16:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160, verbose_name='Name of beer')),
                ('price', models.FloatField(help_text='Indicate the amount in dollars', verbose_name='Price')),
                ('volume', models.FloatField(verbose_name='Volume')),
                ('is_available', models.BooleanField(verbose_name='Availability')),
                ('image', models.ImageField(upload_to='beer_image/', verbose_name='Image')),
                ('url', models.SlugField(max_length=30, unique=True)),
                ('descriptions', models.TextField(blank=True, max_length=5000, verbose_name='Descriptions')),
            ],
            options={
                'verbose_name': 'Beer',
            },
        ),
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Manufacture')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('logo', models.ImageField(upload_to='manufacture/', verbose_name='Logo of manufacture')),
            ],
            options={
                'verbose_name': 'Production',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=0, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Star',
                'verbose_name_plural': 'Stars',
                'ordering': ['-value'],
            },
        ),
        migrations.CreateModel(
            name='Sort_of_beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Sort of beer')),
                ('url', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Sort of beer',
                'verbose_name_plural': 'Sorts of beer',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000, verbose_name='Text')),
                ('beer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='beer.beer', verbose_name='Beer')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='beer.reviews', verbose_name='Parent')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Review',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP address')),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beer.beer', verbose_name='Beer')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beer.ratingstar', verbose_name='Star')),
            ],
            options={
                'verbose_name': 'Rating',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='profile_images/', verbose_name='Image')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, default=datetime.date.today)),
                ('from_country', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профиля пользователей',
            },
        ),
        migrations.CreateModel(
            name='BeerShots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('image', models.ImageField(upload_to='beer_shots_image/', verbose_name='Image')),
                ('description', models.TextField(blank=True, max_length=5000, verbose_name='Description')),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beer.beer', verbose_name='Additional photo of beer')),
            ],
            options={
                'verbose_name': 'Additional photo',
                'verbose_name_plural': 'Additional photos',
            },
        ),
        migrations.AddField(
            model_name='beer',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_manufacturer', to='beer.manufacture', verbose_name='Manufacture'),
        ),
        migrations.AddField(
            model_name='beer',
            name='sort_of_beer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='beer.sort_of_beer', verbose_name='Sort of beer'),
        ),
    ]
