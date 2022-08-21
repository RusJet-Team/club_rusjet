from apps.equipment.models import LastViewedEquipmentItem


def delete_last_viewed_every_day():
    LastViewedEquipmentItem.objects.all().delete()
