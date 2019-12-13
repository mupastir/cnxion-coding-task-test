from django.urls import path

from cnxion.generic_data.views import generic_create_view

app_name = "generic_data"
urlpatterns = [
    path("~add/", view=generic_create_view, name="create"),
]
