from cnxion.generic_data.forms import GenericUniversalForm
from cnxion.generic_data.models import GenericModel


def create_generic_data(form: GenericUniversalForm) -> dict:
    data_type = eval(form.cleaned_data.get("type_field"))
    data = {
        form.cleaned_data.get("title"):
            data_type(form.cleaned_data.get("value"))
    }
    return data


def save_generic_model(data: dict):
    generic_model = GenericModel.objects.create(generic_data=data)
    generic_model.save()
