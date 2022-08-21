from django.conf import settings

from config.utils.decorators import cache_user


def manual_order_app_list(app_dict, admin_site_apps_order):
    app_list = []
    apps = list(app_dict.values())
    for app_name in admin_site_apps_order:
        index = next((index for index, app in enumerate(apps) if app["name"] == app_name), None)
        if index is not None:
            app_list.append(apps.pop(index))

    app_list.extend(apps)
    return app_list


def manual_order_model_list(app, admin_site_models_order):
    app_name = app["name"]
    if app_name in admin_site_models_order:
        ordered_models = []
        models = app["models"]
        for model_name in admin_site_models_order[app_name]:
            index = next((index for index, model in enumerate(models) if model["name"] == model_name), None)
            if index is not None:
                ordered_models.append(models.pop(index))

        ordered_models.extend(models)
        return ordered_models

    app["models"].sort(key=lambda x: x["name"])
    return app["models"]


@cache_user(timelimit=300)
def get_app_list(self, request):
    admin_site_apps_order = getattr(settings, "ADMIN_SITE_APPS_ORDER", None)
    admin_site_models_order = getattr(settings, "ADMIN_SITE_MODELS_ORDER", None)

    app_dict = self._build_app_dict(request)

    if admin_site_apps_order:
        app_list = manual_order_app_list(app_dict, admin_site_apps_order)
    else:
        app_list = sorted(app_dict.values(), key=lambda x: x["name"].lower())

    for app in app_list:
        if admin_site_models_order:
            app["models"] = manual_order_model_list(app, admin_site_models_order)
        else:
            app["models"].sort(key=lambda x: x["name"])

    return app_list
