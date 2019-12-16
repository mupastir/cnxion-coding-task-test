from cnxion.generic_data.forms import GenericModelForm


class TestGenericModelCreationForm:
    def test_valid_data(self):
        form = GenericModelForm(
            {
                "title": 'test',
                "_data": '{"age": 25, "name": "Vasya"}'
            }
        )
        valid = form.is_valid()
        assert valid

    def test_not_valid_data(self):
        form = GenericModelForm(
            {
                "title": 'test',
                "_data": '{"age": "25", "name": "Vasya"}'
            }
        )
        valid = form.is_valid()
        assert not valid
