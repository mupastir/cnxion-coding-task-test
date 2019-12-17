from typing import Iterable

from django import forms

MAPPING_TYPES_FORM_FIELDS = {
    'string': forms.CharField,
    'integer': forms.IntegerField,
    'date': forms.DateField,
    'datetime': forms.DateTimeField,
    'float': forms.FloatField
}


class FormFactory:
    @classmethod
    def create(cls, name: str, scheme: dict, bases: Iterable) -> forms.Form:
        attrs = {k: MAPPING_TYPES_FORM_FIELDS[v['type']]()
                 for k, v in scheme.items()}
        attrs['SCHEME'] = scheme
        return type(name, tuple(bases) or (forms.Form,), attrs)
