from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from shipments.models import Shipment, TemperatureReading

class TestShipmentModels(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
        username="testuser",
        email="test@email.com",
        password="secret"
        )

        self.post = Shipment.objects.create(
            asset_id="replace",
            produce="a product",
            weight=2900,
            pick_up_time=timezone.now(),
            delivery_time=timezone.now(),
            ideal_temperature=27,
            farmer=self.user,
        )

    def test_shipment_str(self):
        entry = Shipment(asset_id="replace")
        self.assertEqual(str(entry), entry.asset_id)

    def test_shipment_content(self):
        self.assertEqual(f"{self.post.asset_id}", "replace")
        self.assertEqual(f"{self.post.produce}", "a product")
        self.assertEqual(f"{self.post.weight}", "a number")
        self.assertEqual(f"{self.post.pick_up_time}", "date and time")
        self.assertEqual(f"{self.post.delivery_time}", "another date and time")
        self.assertEqual(f"{self.post.ideal_temperature}", "any number")
        self.assertEqual(f"{self.post.farmer}", "testuser")

    def test_get_absolute_url(self):
        response = self.client.get(reverse("shipment_detail"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nice content")
        self.assertTemplateUsed(response, "shipment_detail.html")
    
    def test_temperature_str(self):
        value = TemperatureReading(temperature=f"temperature")
        self.assertEqual(str(value), value.temperature)

