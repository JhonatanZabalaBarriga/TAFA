from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Container Model
# -> ASSET_ID : Primary key
class Container(models.Model):
    asset_id = models.CharField(primary_key=True, max_length=250)
    produce = models.CharField(max_length=250)
    weight = models.PositiveIntegerField(blank=False, null=False)
    pick_up_time = models.DateTimeField()
    delivery_time = models.DateTimeField()
    ideal_temperature = models.IntegerField()
    farmer = models.ForeignKey(to=User, on_delete=models.deletion.CASCADE)

    def __str__(self):
        return self.asset_id

class Temperature_Reading(models.Model):
    temperature = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    