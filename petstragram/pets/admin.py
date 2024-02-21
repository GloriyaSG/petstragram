from django.contrib import admin

# Register your models here.
from django.contrib import admin

from petstragram.pets.models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'slug')