from django.views.generic import CreateView

from cnxion.generic_data.utils.views_factory import ViewFactory

from .forms import generic_model_forms_registry

views_registry = []


class CreateGenericModelView(CreateView):
    class Meta:
        abstract = True


generic_model_views_registry = {
    name: ViewFactory.create(name, form, (CreateGenericModelView,))
    for name, form in generic_model_forms_registry.items()
}
