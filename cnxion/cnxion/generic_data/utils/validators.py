from cerberus import Validator
from django.core.exceptions import ValidationError


def validate_data(scheme, data):
    validator = Validator(scheme)
    if not validator.validate(data):
        return validator.errors


def errors_to_validation_error(error_list):
    django_errors = []
    for field_name in error_list.keys():
        for error_string in error_list[field_name]:
            django_errors.append(ValidationError(
                'Field {} {}'.format(field_name, error_string)))
    return django_errors
