from bootstrap_modal_forms.forms import BSModalModelForm

from apps.equipment.models import EquipmentRequest


class EquipmentRequestModelForm(BSModalModelForm):
    class Meta:
        model = EquipmentRequest
        fields = ["name", "email", "phone_number", "text"]
