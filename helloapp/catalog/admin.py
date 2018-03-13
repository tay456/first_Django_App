from django.contrib import admin

# Register your models here.

from django.contrib import admin
from catalog.models import Artists

class ArtistsAdmin(admin.ModelAdmin):
    list_display = ("id", "brand_name", "manager", "contact_number", "contact_email", "country")

admin.site.register(Artists, ArtistsAdmin)
