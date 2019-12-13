from cnxion.generic_data.forms import GenericUniversalForm


def is_valid_generic_model_form(form: GenericUniversalForm) -> bool:
    data_type = form.cleaned_data.get("type_field")
    value = form.cleaned_data.get("value")
    try:
        data_type = eval(data_type)
        data_type(value)
    except ValueError:
        return False
    return True
