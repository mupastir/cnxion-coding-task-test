from django.views.generic import CreateView

from cnxion.generic_data.forms import GenericUniversalForm


class GenericCreateView(CreateView):
    form_class = GenericUniversalForm
