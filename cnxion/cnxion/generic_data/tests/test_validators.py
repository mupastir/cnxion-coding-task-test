from cnxion.generic_data.forms import GenericUniversalForm
from cnxion.generic_data.utils.choices import DATA_TYPE_CHOICES
from cnxion.generic_data.utils.validators import is_valid_generic_model_form


class TestGenericDataValidator:

    def test_valid_int_data(self):
        form = GenericUniversalForm({
            "title": "Age",
            "type_field": DATA_TYPE_CHOICES.number.value[0],
            "value": "26"
        })
        form.is_valid()
        assert is_valid_generic_model_form(form)

    def test_valid_str_data(self):
        form = GenericUniversalForm(data={
            "title": "Name",
            "type_field": DATA_TYPE_CHOICES.string.value[0],
            "value": "Alexa"
        })
        form.is_valid()
        assert is_valid_generic_model_form(form)

    def test_not_valid_str_data(self):
        form = GenericUniversalForm(data={
            "title": "Name",
            "type_field": DATA_TYPE_CHOICES.number.value[0],
            "value": "Alexa"
        })
        form.is_valid()
        assert not is_valid_generic_model_form(form)
