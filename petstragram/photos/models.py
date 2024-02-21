from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from petstragram.pets.models import Pet
from petstragram.photos.validators import validate_file_size



# Create your models here.
class PetPhoto(models.Model):
    MIN_DESCRIPTION = 10
    MAX_DESCRIPTION = 300
    MAX_LOCATION = 30

    photo = models.ImageField(upload_to='pet_photos/',
                              blank=False,
                              null=False,
                              validators=(validate_file_size,))
    description = models.TextField(
        blank=True,
        null=True,
        max_length=MAX_DESCRIPTION,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION),
        ))

    location = models.CharField(max_length=MAX_LOCATION,
                                null=True,
                                blank=True,)

    pets = models.ManyToManyField(Pet, blank=True)

    date_of_publication = models.DateField(auto_now=True)
