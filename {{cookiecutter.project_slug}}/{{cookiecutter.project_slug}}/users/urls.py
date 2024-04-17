from django.urls import path

from pyutils.rest_framework.viewsets import UserViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter
from pyutils.django.viewsets import router_register_viewset
from {{ cookiecutter.project_slug }}.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]



if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router_register_viewset(router, UserViewSet)

urlpatterns = [] + router.urls
