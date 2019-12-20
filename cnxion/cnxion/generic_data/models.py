from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models

from .utils.validators import validate_data


class GenericModel(models.Model):
    _data = JSONField(null=True)
    data_type = models.CharField(max_length=50, null=False)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        errors = validate_data(settings.SCHEME[self.data_type], value)
        if errors is None:
            self._data = value
        else:
            raise ValueError(
                'Could not set to new value. Reasons: {}'.format(errors))

    def __str__(self):
        return str(self._data)
