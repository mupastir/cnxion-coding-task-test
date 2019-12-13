from django import forms
from django.forms import formset_factory

from cnxion.generic_data.utils.choices import DATA_TYPE_CHOICES


class GenericUniversalForm(forms.Form):
    title = forms.CharField(label="Title", max_length=50)
    type_field = forms.ChoiceField(label='Type data',
                                   choices=[x.value for x in
                                            DATA_TYPE_CHOICES])
    value = forms.CharField(label="Value", max_length=100)


GenericFormset = formset_factory(GenericUniversalForm, extra=1)
