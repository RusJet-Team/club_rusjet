from django.urls import path

from apps.equipment.views import EquipmentView, ShopView

urlpatterns = [
    path("equipment/", EquipmentView.as_view(), name="equipment"),
    path("shop/", ShopView.as_view(), name="shop"),
]
