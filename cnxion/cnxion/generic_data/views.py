from django.views.generic import CreateView

from cnxion.generic_data.forms import GenericUniversalForm
from cnxion.generic_data.models import GenericModel


class GenericCreateView(CreateView):

    model = GenericModel
    form_class = GenericUniversalForm


generic_create_view = GenericCreateView.as_view()
