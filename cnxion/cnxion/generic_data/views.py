from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import GenericModelForm


class CreateGenericModelView(CreateView):
    form_class = GenericModelForm
    template_name = 'generic_data/genericmodel_form.html'
    success_url = reverse_lazy('generic_data:create')
