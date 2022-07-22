from django.views.generic import ListView

from .models import Shipment, TemperatureReading

class ShipmentListView(ListView):
    model = Shipment
    template_name = 'shipment_list.html'
