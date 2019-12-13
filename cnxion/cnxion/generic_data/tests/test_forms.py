from cnxion.generic_data.forms import GenericUniversalForm
from cnxion.generic_data.utils.choices import DATA_TYPE_CHOICES


class TestGenericDataCreationForm:
    def test_valid_int_data(self):
        form = GenericUniversalForm({
            "title": "Age",
            "type_field": DATA_TYPE_CHOICES.number.value[0],
            "value": "26"
        })
        valid = form.is_valid()
        assert valid

        form = GenericUniversalForm({
            "title": "Age",
            "type_field": DATA_TYPE_CHOICES.number.value,
            "value": 26.0
        })
        valid = form.is_valid()
        assert not valid
