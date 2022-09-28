#Mock create/update/delete_asset
from unittest import mock
from django.test import TestCase
from shipments.signals import shipment_pre_save, shipment_pre_delete
from shipments.models import Shipment 

class TestSignal(TestCase):
    @mock.patch("shipments.signals.shipment_pre_save")
    def test_create_asset(self, mock_get):
        
        mock_response = mock.Mock()

        attributes = {
            "asset_id": f"{Shipment.asset_id}",
            "produce": f"{Shipment.produce}",
            "weight": f"{Shipment.weight}",
            "pick_up_time": f"{Shipment.pick_up_time}",
            "delivery_time": f"{Shipment.delivery_time}",
            "ideal_temp": f"{Shipment.ideal_temperature}",
            "farmer": f"{Shipment.farmer}",
        }

        data = {
            "type": "assets",
            "id": "asset_id",
            "attributes": f"{attributes}",
        }
        

        mock_response.json.return_value = data
        mock_response.status_code = 200

        mock_get.return_value = mock_response

    @mock.patch("shipments.signals.shipment_pre_delete")
    def test_delete_asset(self, mock_get):

        mock_response = mock.Mock()
        mock_response.status_code = 200

        mock_get.return_value - mock_response

