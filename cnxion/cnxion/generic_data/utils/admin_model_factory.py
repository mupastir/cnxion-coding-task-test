from typing import Iterable

from django.forms import forms


class AdminModelFactory:
    @classmethod
    def create(cls, name: str, form: forms.Form, bases: Iterable):
        attrs = {'form': form}
        return type(f'{name}GenericAdmin', tuple(bases), attrs)
