from django.urls import path

from apps.equipment.views import EquipmentDetailView, EquipmentView

urlpatterns = [
    path("equipment/", EquipmentView.as_view(), name="equipment"),
    path("equipment-detail/", EquipmentDetailView.as_view(), name="equipment-detail"),
]
