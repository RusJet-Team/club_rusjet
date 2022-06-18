from django.urls import include, path

from apps.equipment.views import (
    EquipmentBrendDetailView,
    EquipmentCategoryDetailView,
    EquipmentCategoryListView,
    EquipmentItemDetailView,
    EquipmentSubCategoryDetailView,
)

equipments_urls = [
    path(
        "",
        EquipmentCategoryListView.as_view(),
        name="equipments",
    ),
    path(
        "<slug:category_slug>/",
        EquipmentCategoryDetailView.as_view(),
        name="equipment-categories",
    ),
    path(
        "<slug:category_slug>/<slug:subcategory_slug>/",
        EquipmentSubCategoryDetailView.as_view(),
        name="equipment-subcategories",
    ),
    path(
        "<slug:category_slug>/<slug:subcategory_slug>/<slug:brend_slug>/",
        EquipmentBrendDetailView.as_view(),
        name="equipment-brends",
    ),
    path(
        "<slug:category_slug>/<slug:subcategory_slug>/<slug:brend_slug>/<int:pk>/",
        EquipmentItemDetailView.as_view(),
        name="equipment-item",
    ),
]

urlpatterns = [
    path("equipment/", include(equipments_urls)),
]
