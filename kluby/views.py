from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, UpdateView, ListView

from .models import Klub, Competition


def index(request):
    context = {
        "kluby": Klub.objects.order_by("name")[:5],
        'competitions': Competition.objects.order_by('name').all()
    }
    return render(request, "index.html", context=context)


class FilmListView(ListView):
    model = Klub
    context_object_name = 'klubs_list'
    template_name = 'klub/list.html'


class KlubDetailView(DetailView):
    model = Klub
    context_object_name = 'klub_detail'
    template_name = 'klub/detail.html'


class KlubDelete(DeleteView):
    model = Klub
    success_url = reverse_lazy('kluby')
