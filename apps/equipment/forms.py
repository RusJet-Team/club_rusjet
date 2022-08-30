from django import forms

from apps.equipment.models import EquipmentRequest


class EquipmentRequestModelForm(forms.ModelForm):
    class Meta:
        model = EquipmentRequest
        fields = ["name", "email", "phone_number", "text"]
