from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.list_events, name='list_events'),
    path('<int:id>', views.detail, name='detail'),
]
