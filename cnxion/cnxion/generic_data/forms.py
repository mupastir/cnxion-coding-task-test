import json
from json.decoder import JSONDecodeError

from django.conf import settings
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.forms.fields import CharField
from django.forms.widgets import Textarea

from .models import GenericModel
from .utils.validators import errors_to_validation_error, validate_data


class GenericModelForm(ModelForm):
    scheme = CharField(widget=Textarea, disabled=True, initial=settings.SCHEME)

    def clean__data(self):
        try:
            scheme_dict = json.loads(self.data['_data'])
        except JSONDecodeError as e:
            raise ValidationError(
                'Could not parse json.Reason: {}'.format(e.msg))

        self.cleaned_data['_data'] = scheme_dict
        scheme = self.instance.scheme \
            if self.instance is not None else settings.SCHEME
        data = self.cleaned_data['_data']
        errors = validate_data(scheme, data)
        if errors is None:
            self.cleaned_data['_data'] = data
            return self.cleaned_data
        django_error = errors_to_validation_error(errors)
        raise ValidationError(django_error)

    def clean(self):
        self.clean__data()

    class Meta:
        model = GenericModel
        fields = ('title', '_data')
