from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from apps.equipment.models import EquipmentBrend, EquipmentCategory, EquipmentItem, EquipmentSubCategory


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
        return EquipmentSubCategory.objects.filter(subcategory_slug=self.kwargs["subcategory_slug"]).values("name")

    def get_context_data(self, **kwargs):
        context = {}
        super().get_context_data()
        context["brends"] = EquipmentBrend.objects.filter(subcategory__subcategory_slug=self.kwargs["subcategory_slug"])
        print(context)
        return super().get_context_data(**context)


class EquipmentBrendDetailView(DetailView):

    model = EquipmentBrend
    slug_field = "brend_slug"
    slug_url_kwarg = "brend_slug"
    template_name = "equipment/equipments-brends.html"

    def get_queryset(self):
        return EquipmentBrend.objects.filter(brend_slug=self.kwargs["brend_slug"]).values("name")

    def get_context_data(self, **kwargs):
        context = {}
        super().get_context_data()
        context["objects"] = EquipmentItem.objects.filter(brend__brend_slug=self.kwargs["brend_slug"])
        print(context)
        return super().get_context_data(**context)


class EquipmentItemDetailView(DetailView):

    model = EquipmentItem
    template_name = "equipment/equipments-detail.html"


# class SearchNewsResultsView(ListView):
#     model = News
#     template_name = "news/search_results.html"

#     def get_queryset(self):
#         query = self.request.GET.get("search")
#         object_list = News.objects.filter(
#             Q(name__icontains=query) | Q(title__icontains=query) | Q(text__icontains=query)
#         )
#         return object_list
