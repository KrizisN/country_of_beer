from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Sort_of_beer(models.Model):
    """Beer varieties model"""
    name = models.CharField('Sort of beer', max_length=30)
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sort of beer'
        verbose_name_plural = 'Sorts of beer'


class Manufacture(models.Model):
    """Manufacture"""
    name = models.CharField('Manufacture', max_length=150)
    description = models.TextField('Description', blank=True)
    logo = models.ImageField('Logo of manufacture', upload_to='manufacture/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Production'


class Profile(models.Model):
    """Additional model 1t1 for information"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField('Image', upload_to='profile_images/', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(blank=True, default=date.today)
    from_country = models.CharField(max_length=50, blank=True)

    def get_absolute_url(self):
        return reverse("profile_settings", kwargs={"pk": self.pk})

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профиля пользователей"


class Beer(models.Model):
    """"Beer"""
    name = models.CharField("Name of beer", max_length=160)
    sort_of_beer = models.ForeignKey(Sort_of_beer, verbose_name="Sort of beer", on_delete=models.SET_NULL, null=True)
    manufacturer = models.ForeignKey(Manufacture, verbose_name="Manufacture",on_delete=models.CASCADE, related_name="main_manufacturer")
    price = models.FloatField("Price", help_text="Indicate the amount in dollars")
    volume = models.FloatField("Volume")
    is_available = models.BooleanField("Availability")
    image = models.ImageField("Image", upload_to='beer_image/')
    url = models.SlugField(max_length=30, unique=True)
    descriptions = models.TextField("Descriptions", blank=True, max_length=5000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("beer_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Beer"


class RatingStar(models.Model):
    """Rating Star"""
    value = models.PositiveSmallIntegerField("Value", default=0)

    def __str__(self):
        return f"{self.value}"

    class Meta:
        verbose_name = "Star"
        verbose_name_plural = "Stars"
        ordering = ["-value"]


class Rating(models.Model):
    """Rating"""
    ip = models.CharField("IP address", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Star")
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE, verbose_name="Beer")

    def __str__(self):
        return f"{self.beer} - {self.star}"

    class Meta:
        verbose_name = "Rating"


class Reviews(models.Model):
    """"Reviews"""
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField("Text", max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Parent', on_delete=models.SET_NULL, blank=True, null=True)
    beer = models.ForeignKey(Beer, verbose_name="Beer", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Review"


class BeerShots(models.Model):
    """Additional photo of beer"""
    name = models.CharField("Name", max_length=100)
    image = models.ImageField("Image", upload_to='beer_shots_image/')
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE, verbose_name="Additional photo of beer")
    description = models.TextField("Description", blank=True, max_length=5000)

    def __str__(self):
        return f"{self.name} - {self.beer}"

    class Meta:
        verbose_name = "Additional photo"
        verbose_name_plural = "Additional photos"