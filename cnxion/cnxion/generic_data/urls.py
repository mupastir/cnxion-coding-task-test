from django.urls import path

from cnxion.generic_data.views import generic_model_views_registry

app_name = "generic_data"
urlpatterns = [
    path(f"add-{name.lower()}/",
         view=view.as_view(),
         name=f"create_{name.lower()}")
    for name, view in generic_model_views_registry.items()
]
