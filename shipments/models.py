from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# Container Model
# -> ASSET_ID : Primary key

#TODO customize save()


class Shipment(models.Model):
    asset_id = models.CharField(primary_key=True, max_length=250)
    produce = models.CharField(max_length=250)
    weight = models.PositiveIntegerField(blank=False, null=False)
    pick_up_time = models.DateTimeField()
    delivery_time = models.DateTimeField()
    ideal_temperature = models.IntegerField()
    farmer = models.ForeignKey(to=User, on_delete=models.deletion.CASCADE)

    def __str__(self) -> str:
        return f"<ShipmentInstance {self.asset_id}>"

    def get_absolute_url(self):
        return reverse('shipment_detail', args=[str(self.pk)])

class TemperatureReading(models.Model):
    temperature = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    shipment = models.ForeignKey(to=Shipment, on_delete=models.deletion.CASCADE)

    def __str__(self) -> str:
        return f"<TemperatureReading {self.shipment}>"
