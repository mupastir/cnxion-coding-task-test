from typing import Iterable

from django.forms import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView


class ViewFactory:
    @classmethod
    def create(cls, name: str, form: forms.Form, bases: Iterable):
        attrs = {
            'form_class': form,
            'success_url': reverse_lazy(f'generic_data:create_{name.lower()}'),
            'template_name': 'generic_data/genericmodel_form.html',
            'extra_context': {
                'form_post_url': f'generic_data:create_{name.lower()}'
            }
        }
        return type(f'{name}CreateView', tuple(bases) or (CreateView,), attrs)
