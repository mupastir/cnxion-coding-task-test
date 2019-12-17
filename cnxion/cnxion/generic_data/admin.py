from django.contrib import admin

from cnxion.generic_data.forms import GenericModelForm

from .models import GenericModel


@admin.register(GenericModel)
class GenericAdmin(admin.ModelAdmin):
    form = GenericModelForm
