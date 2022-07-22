from django.contrib import admin

from .models import Shipment, TemperatureReading

admin.site.register(Shipment)
admin.site.register(TemperatureReading)
