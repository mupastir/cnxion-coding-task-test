from django import forms

from cnxion.generic_data.models import GenericModel


class GenericUniversalForm(forms.ModelForm):
    class Meta:
        model = GenericModel
        fields = ['generic_data']
