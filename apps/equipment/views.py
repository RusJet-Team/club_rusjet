import json

from django.conf import settings
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView, MultipleObjectMixin

from apps.equipment.forms import EquipmentRequestModelForm
from apps.equipment.models import (
    EquipmentBrend,
    EquipmentCategory,
    EquipmentItem,
    EquipmentSubCategory,
    LastViewedEquipmentItem,
)


class EquipmentCategoryListView(ListView):

    model = EquipmentCategory
    template_name = "equipment/equipments.html"


class EquipmentCategoryDetailView(DetailView):

    model = EquipmentCategory
    slug_field = "category_slug"
    slug_url_kwarg = "category_slug"
    template_name = "equipment/equipments-categories.html"

    def get_queryset(self):
        return EquipmentCategory.objects.filter(category_slug=self.kwargs["category_slug"]).values("name")

    def get_context_data(self, **kwargs):
        self.object["category_slug"] = self.kwargs["category_slug"]
        context = {}
        super().get_context_data()
        context["subcategories"] = EquipmentSubCategory.objects.filter(
            category__category_slug=self.kwargs["category_slug"]
        )
        return super().get_context_data(**context)


class EquipmentSubCategoryDetailView(DetailView):

    model = EquipmentSubCategory
    slug_field = "subcategory_slug"
    slug_url_kwarg = "subcategory_slug"
    template_name = "equipment/equipments-subcategories.html"

    def get_queryset(self):
        return EquipmentSubCategory.objects.filter(subcategory_slug=self.kwargs["subcategory_slug"]).all()

    def get_context_data(self, **kwargs):
        context = {}
        super().get_context_data()
        context["brends"] = EquipmentBrend.objects.filter(subcategory__subcategory_slug=self.kwargs["subcategory_slug"])
        return super().get_context_data(**context)


class EquipmentBrendDetailView(MultipleObjectMixin, DetailView):

    model = EquipmentBrend
    slug_field = "brend_slug"
    slug_url_kwarg = "brend_slug"
    template_name = "equipment/equipments-brends.html"
    paginate_by = 6

    def get_queryset(self):
        return EquipmentBrend.objects.filter(brend_slug=self.kwargs["brend_slug"]).all()

    def get_context_data(self, **kwargs):
        object_list = EquipmentItem.objects.filter(brend__brend_slug=self.kwargs["brend_slug"])
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class EquipmentItemDetailView(DetailView):

    model = EquipmentItem
    template_name = "equipment/equipments-detail.html"

    def get_object(self):
        obj = super().get_object()
        if not self.request.session or not self.request.session.session_key:
            self.request.session.save()
        LastViewedEquipmentItem.objects.get_or_create(session=self.request.session.session_key, equipment_item=obj)
        last_viewed = LastViewedEquipmentItem.objects.filter(session=self.request.session.session_key)
        if last_viewed.count() > 5:
            last_viewed.first().delete()
        return obj


class EquipmentItemResultsView(ListView):
    model = EquipmentItem
    template_name = "equipment/equip_search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("search")
        search_vector = SearchVector("name", "title", "brend__name")
        search_query = SearchQuery(query)
        object_list = (
            EquipmentItem.objects.annotate(search=search_vector, rank=SearchRank(search_vector, search_query))
            .filter(search=search_query)
            .order_by("-rank")
        )
        return object_list


def add_request(request):
    if request.method == "POST":
        form = EquipmentRequestModelForm(request.POST)
        if form.is_valid():
            request_equipment = form.save()
            subject = f"Поступил запрос на оборудование от {form.data.get('name')} с rusjet.ru"
            msg_plain = render_to_string("equipment/email.txt", form.data)
            msg_html = render_to_string("equipment/email.html", form.data)
            send_mail(
                subject,
                msg_plain,
                settings.EMAIL_HOST_USER,
                [settings.DEFAULT_FROM_EMAIL],
                html_message=msg_html,
            )
            return HttpResponse(
                status=204, headers={"HX-Trigger": json.dumps({"showMessage": f"{request_equipment.name} added."})}
            )
    else:
        form = EquipmentRequestModelForm()
    return render(
        request,
        "equipment/create_request.html",
        {
            "form": form,
        },
    )
