from django.urls import path

from cnxion.generic_data.views import CreateGenericModelView

app_name = "generic_data"
urlpatterns = [
    path("add/", view=CreateGenericModelView.as_view(), name="create"),
]
