from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver 
from shipments.models import Shipment
from shipments.fetch_client import create_asset, delete_asset, update_asset

@receiver(pre_save, sender=Shipment)
def shipment_pre_save(sender, instance, *args, **kwargs):

    print(instance.asset_id)
    print(instance)
    
    if instance.asset_id == "replace":
        data = create_asset()
        instance.asset_id = data['id']
        print(f"{instance.asset_id} was created")

    else:
        attributes = {
            "asset_id": instance.asset_id,
            "produce": instance.produce,
            "weight": instance.weight,
            "pick_up_time": instance.pick_up_time,
            "delivery_time": instance.delivery_time,
            "ideal_temp": instance.ideal_temperature,
            "farmer": instance.farmer,
        }

        update = update_asset(instance.asset_id, attributes)
        print(f"{instance.asset_id} was updated")

@receiver(pre_delete, sender=Shipment)
def shipment_pre_delete(sender, instance, *args, **kwargs):
    delete = delete_asset(instance.asset_id)
    print(f"{instance.asset_id} has been removed")