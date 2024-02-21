from django.contrib import admin

from petstragram.photos.models import PetPhoto


# Register your models here.
@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass