from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Shipment, TemperatureReading

class ShipmentListView(ListView):
    model = Shipment
    template_name = 'shipment_list.html'

class ShipmentDetailView(DetailView): 
    model = Shipment
    template_name = 'shipment_detail.html'

class ShipmentUpdateView(UpdateView): 
    model = Shipment
    fields = ('produce', 'weight', 'pick_up_time', 'delivery_time', 'ideal_temperature',)
    template_name = 'shipment_edit.html'

class ShipmentDeleteView(DeleteView):
    model = Shipment
    template_name = 'shipment_delete.html'
    success_url = reverse_lazy('shipment_list')
