from django.shortcuts import render
from .models import Event

def index(request):
    context = { 'count': Event.objects.count() }
    return render(request = request, template_name = "events/index.html", context = context)
