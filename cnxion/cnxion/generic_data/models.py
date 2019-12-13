from django.db import models
from django_extensions.db.fields.json import JSONField


class GenericModel(models.Model):
    generic_data = JSONField()

    def __str__(self):
        return str(self.generic_data)
