from django.http import HttpResponseForbidden

from mapapp.models import Map


def map_ownership_required(func):
    def decorated(request, *args, **kwargs):
        mapping = Map.objects.get(pk=kwargs['pk'])
        if not mapping.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated

