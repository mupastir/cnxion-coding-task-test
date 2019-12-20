from django.conf import settings
from django.forms import ModelForm

from cnxion.generic_data.models import GenericModel

from .utils.form_factory import FormFactory


class BaseModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.data:
            for field in self.fields:
                self.fields[field].initial = self.instance._data[field]

    def save(self, commit=True):
        self.instance.data_type = self.data_type
        self.instance.data = self.cleaned_data
        return super().save(commit)

    class Meta:
        model = GenericModel
        fields = []


generic_model_forms_registry = {
    name: FormFactory.create(name, scheme, (BaseModelForm,))
    for name, scheme in settings.SCHEME.items()
}
