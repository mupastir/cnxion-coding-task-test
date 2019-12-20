from typing import Iterable

from django import forms

MAPPING_TYPES_FORM_FIELDS = {
    'string': forms.CharField,
    'integer': forms.IntegerField,
    'float': forms.FloatField,
    'bool': forms.BooleanField
}


class FormFactory:
    @classmethod
    def create(cls, name: str,
               scheme: dict,
               bases: Iterable) -> type(forms.Form):
        attrs = {k: MAPPING_TYPES_FORM_FIELDS[v['type']]()
                 for k, v in scheme.items()}
        attrs['SCHEME'] = scheme
        attrs['data_type'] = name
        return type(f'{name}Form', tuple(bases) or (forms.Form,), attrs)
