from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

# from mooving_oms.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


urlpatterns = [
    path("home/", include("{{cookiecutter.project_slug}}.home.urls")),
    path("users/", include("{{cookiecutter.project_slug}}.users.urls")),

]

app_name = "api"
urlpatterns += router.urls
