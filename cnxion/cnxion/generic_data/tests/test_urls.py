from django.urls import resolve, reverse


def test_update():
    assert reverse("generic_data:create") == "/generic-data/~add/"
    assert resolve("/generic-data/~add/").view_name == "generic_data:create"
