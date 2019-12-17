from django.conf import settings
from django.forms import ModelForm

from cnxion.generic_data.models import GenericModel

from .utils.form_factory import FormFactory


class BaseModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            for field in self.fields:
                self.fields[field].initial = self.instance._data[field]

    def save(self, commit=True):
        self.instance.data = self.cleaned_data
        return super().save(commit)

    class Meta:
        model = GenericModel
        fields = []


GenericModelForm = FormFactory.create(
    'GenericModelForm', settings.SCHEME, (BaseModelForm,)
)
