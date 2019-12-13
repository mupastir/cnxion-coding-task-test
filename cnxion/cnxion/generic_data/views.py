from django.shortcuts import redirect, render

from cnxion.generic_data.forms import GenericFormset
from cnxion.generic_data.services import create_generic_data, save_generic_model
from cnxion.generic_data.utils.validators import is_valid_generic_model_form


def generic_create_view(request):
    template_name = 'generic_data/genericmodel_form.html'
    heading_message = 'Add generic data'
    if request.method == 'GET':
        formset = GenericFormset(request.GET or None)
    elif request.method == 'POST':
        formset = GenericFormset(request.POST)
        if formset.is_valid():
            data = {}
            for form in formset:
                if not is_valid_generic_model_form(form):
                    break
                data.update(create_generic_data(form))
            save_generic_model(data)
            return redirect('home')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })
