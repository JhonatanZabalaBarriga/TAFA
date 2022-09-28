from unittest import mock

from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from shipments.models import Shipment, TemperatureReading
from shipments.signals import update_asset

class TestShipmentModels(TestCase):

    def setUp(self):
        self.patcher = mock.patch("shipments.signals.update_asset", return_value = {"asset_id": "nope"})
        self.patcher.start()
        
        self.date = timezone.now()
        self.asset_id = "test"
        self.temperature = 28

        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret"
        )
        pre_save.disconnect(sender=Shipment)
        self.shipment = Shipment.objects.create(
            asset_id=self.asset_id,
            produce="a product",
            weight=2900,
            pick_up_time=self.date,
            delivery_time=self.date,
            ideal_temperature=self.temperature,
            farmer=self.user,
        )

    def test_shipment_str(self):
        self.assertEqual(str(self.shipment), f"Shimpent with ID: {self.asset_id}")
    
    def test_shipment_content(self):
        self.assertEqual(f"{self.shipment.asset_id}", "test")
        self.assertEqual(f"{self.shipment.produce}", "a product")
        self.assertEqual(self.shipment.weight, 2900)
        self.assertEqual(self.shipment.pick_up_time, self.date)
        self.assertEqual(self.shipment.delivery_time, self.date)
        self.assertEqual(self.shipment.ideal_temperature, self.temperature)
        self.assertEqual(f"{self.shipment.farmer}", "testuser")
        
    def test_get_absolute_url(self):
        response = self.client.get(self.shipment.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shipment_detail.html")
    
    def test_temperature_str(self):
        temperature_reading = TemperatureReading(temperature=self.temperature)
        self.assertEqual(str(temperature_reading), f"Temperature Reading: {self.temperature}")

