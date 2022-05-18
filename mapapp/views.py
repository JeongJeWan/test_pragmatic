from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView

from commentapp.forms import CommentCreationForm
from mapapp.decorators import map_ownership_required
from mapapp.forms import MapCreationForm
from mapapp.models import Map


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class MapCreateView(CreateView):
    model = Map
    form_class = MapCreationForm
    template_name = 'mapapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mapapp:detail', kwargs={'pk': self.object.pk})


class MapDetailView(DetailView, FormMixin):
    model = Map
    form_class = CommentCreationForm
    context_object_name = 'target_map'
    template_name = 'mapapp/detail.html'


@method_decorator(map_ownership_required, 'get')
@method_decorator(map_ownership_required, 'post')
class MapUpdateView(UpdateView):
    model = Map
    context_object_name = 'target_map'
    form_class = MapCreationForm
    template_name = 'mapapp/update.html'

    def get_success_url(self):
        return reverse('mapapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(map_ownership_required, 'get')
@method_decorator(map_ownership_required, 'post')
class MapDeleteView(DeleteView):
    model = Map
    context_object_name = 'target_map'
    success_url = reverse_lazy('mapapp:list')
    template_name = 'mapapp/delete.html'


class MapListView(ListView):
    model = Map
    context_object_name = 'map_list'
    template_name = 'mapapp/list.html'
    paginate_by = 5
