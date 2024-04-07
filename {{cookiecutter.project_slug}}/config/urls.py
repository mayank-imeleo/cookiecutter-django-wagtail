from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
{%- if cookiecutter.use_async == 'y' %}
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
{%- endif %}
from django.urls import include, path, re_path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.views.generic import RedirectView
from {{ cookiecutter.project_slug }}.search import views as search_views  # noqa isort:skip
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from pyutils.rest_framework.views import AuthTokenUserIdAPIView
from django.conf import settings
from django.urls import path
from pyutils.rest_framework.viewsets import UserViewSet
from pyutils.django.viewsets import router_register_viewset
from rest_framework.routers import DefaultRouter, SimpleRouter

urlpatterns = [

                  path(
                      "",
                      RedirectView.as_view(url=f"{settings.WAGTAIL_ADMIN_URL}"),
                      name="home",
                  ),

                  # Wagtail Admin
                  path(settings.WAGTAIL_ADMIN_URL, include(wagtailadmin_urls)),

                  # Django Admin
                  path(settings.DJANGO_ADMIN_URL, admin.site.urls),

                  # Documents
                  re_path(r"^documents/", include(wagtaildocs_urls)),

                  # Search
                  re_path(r"^search/$", search_views.search, name="search"),

                  # Users
                  path("users/",
                       include("{{cookiecutter.project_slug}}.users.urls", namespace="users")),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

{%- if cookiecutter.use_async == 'y' %}
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()
{%- endif %}

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    path("api/v2/", wagtail_api_router.urls),
    # DRF auth token
    path("auth-token/", AuthTokenUserIdAPIView.as_view()),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

if settings.DEBUG:
    # Wagtail settings: Serve static and media files from development server
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
        path("__reload__/", include("django_browser_reload.urls")),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

urlpatterns += [
    path("", include(wagtail_urls)),
]

admin.site.site_header = "Imeleo Admin Header"
admin.site.site_title = "Imeleo Admin Site Title"
admin.site.index_title = "Imeleo Admin Index Title"
