from django.views.generic import ListView

from .models import Container, Temperature_Reading

class ContainerListView(ListView):
    model = Container
    template_name = 'container_list.html'
