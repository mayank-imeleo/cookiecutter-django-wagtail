from django.apps import AppConfig


class SearchAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{cookiecutter.project_slug}}.search"
    label = "search"

    def ready(self):
        try:
            import {{cookiecutter.project_slug}}.search.signals # noqa: F401
        except ImportError:
            pass
