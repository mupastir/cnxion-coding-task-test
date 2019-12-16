from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models

from .utils.validators import validate_data


class GenericModel(models.Model):
    title = models.CharField(max_length=32, null=False)
    _data = JSONField(null=True)
    scheme = JSONField(default=settings.SCHEME)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        errors = validate_data(self.scheme, value)
        if errors is None:
            self._data = value
        else:
            raise ValueError(
                'Could not set to new value. Reasons: {}'.format(errors))

    def __str__(self):
        return self.title
