from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Pet(models.Model):
    MAX_NAME = 30
    name = models.CharField(
        max_length=MAX_NAME,
        blank=False,
        null = False)

    pet_photo = models.URLField()
    date_of_birth = models.DateField(
        null=True,
        blank=False)
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        editable=False,)

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.pk}")

        super().save(*args, **kwargs)

