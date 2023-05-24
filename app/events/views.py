from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import render

from .models import Event


def index(request):
    context = { 'count': Event.objects.count() }
    return render(request = request, template_name = "events/index.html", context = context)

def list_events(request):
    events = Event.objects.all().values()
    return JsonResponse(data = list(events), safe = False)

def detail(request, id):
    event = Event.objects.get(pk = id)
    return JsonResponse(data = model_to_dict(event))
