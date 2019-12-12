from django.urls import path

from cnxion.generic_data.views import GenericCreateView

app_name = "generic_data"
urlpatterns = [
    path("~add-data/", view=GenericCreateView.as_view(), name="create"),
]
