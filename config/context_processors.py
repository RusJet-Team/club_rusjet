import datetime as dt

from apps.services.models import ServiceItem


def year(request):
    """Добавляет переменную с текущим годом."""
    year = dt.datetime.now().year
    return {"year": year}


def services(request):
    """Добавляет названия сервисов в NavBar."""
    services_names = ServiceItem.objects.values("name", "slug")
    return {"services_names": services_names}
