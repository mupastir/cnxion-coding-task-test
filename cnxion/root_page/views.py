from django.conf import settings
from django.views.generic import TemplateView


class RootView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generic_data_urls'] = {
            name: f'generic_data:create_{name.lower()}'
            for name in settings.SCHEME.keys()
        }
        return context
