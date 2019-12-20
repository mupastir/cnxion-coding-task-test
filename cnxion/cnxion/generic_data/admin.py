from django.contrib import admin

from .models import GenericModel


@admin.register(GenericModel)
class GenericAdmin(admin.ModelAdmin):
    pass
