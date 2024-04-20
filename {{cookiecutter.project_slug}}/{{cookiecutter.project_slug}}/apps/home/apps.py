from django.apps import AppConfig


class HomeAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{cookiecutter.project_slug}}.home"
    label = "home"

    def ready(self):
        try:
            import {{cookiecutter.project_slug}}.home.signals # noqa: F401
        except ImportError:
            pass
