from django.views.generic import TemplateView
from .models import Service, Team

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['Service'] = Service.objects.order_by('?').all()
        context['Team'] = Team.objects.order_by('?').all()
        return context