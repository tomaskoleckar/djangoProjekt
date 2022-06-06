from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, ListView

from .models import Klub, Competition


def index(request):
    context = {
        "kluby": Klub.objects.order_by("name")[:5],
        'competitions': Competition.objects.order_by('name').all()
    }
    return render(request, "index.html", context=context)


class KlubListView(ListView):

    model = Klub
    context_object_name = 'klubs_list'
    template_name = 'klub/list.html'


    def get_queryset(self):
        if 'competition_name' in self.kwargs:
            return Klub.objects.filter(competitions__name=self.kwargs['competition_name']).all()
        else:
            # ... v opačném případě jsou vybrány všechny objekty (filmy)
            return Klub.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_films'] = len(self.get_queryset())
        if 'competition_name' in self.kwargs:
            # ... šabloně budou prostřednictvím kontextu předány proměnné 'view_title' a 'view_head', které budou obsahovat informace
            # o aktuálně vybraném žánru
            context['view_title'] = f"Soutěž: {self.kwargs['competition_name']}"
            context['view_head'] = f"Soutěž: {self.kwargs['competition_name']}"
        else:
            # ... v opačném případě budou předány stejné proměnné s obecnějším popisem
            # o aktuálně vybraném žánru
            context['view_title'] = 'Kluby'
            context['view_head'] = 'Přehled soutěží'
        return context

class KlubDetailView(DetailView):
    model = Klub
    context_object_name = 'klub_detail'
    template_name = 'klub/detail.html'


class KlubDelete(DeleteView):
    model = Klub
    success_url = reverse_lazy('kluby')
