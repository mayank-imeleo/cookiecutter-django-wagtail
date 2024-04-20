import os
import time

from django.conf import settings
from django.templatetags.static import static
from django.utils.html import format_html
from wagtail import hooks

summary_items_to_append = []


def _js_link(js_file):
    t = int(time.time())
    return format_html('<script src="{}?{}">', static(js_file), t)


# Insert Global Admin CSS
@hooks.register("insert_global_admin_css")
def global_admin_css():
    if settings.DEBUG:
        css_files = [
            "css/global.css",
        ]
    else:
        css_files = [
            "css/global.min.css",
        ]
    t = int(time.time())
    css_markup = [
        format_html('<link rel="stylesheet" href="{}?{}">', static(f), t)
        for f in css_files
    ]
    return "".join(css_markup)


# Causing JS bugs in Wagtail
# @hooks.register("insert_global_admin_js")
# def global_admin_js():
#     js_files = [
#         "js/global.js",
#     ]
#     return "".join([_js_link(f) for f in js_files])


@hooks.register("insert_editor_js")
def editor_js():
    js_files = [
        "js/editor.js",
    ]

    return "".join([_js_link(f) for f in js_files])


#
@hooks.register("construct_main_menu")
def hide_snippets_menu_item(request, menu_items):
    hide_items = ["images", "documents"]
    if not request.user.is_superuser:
        hide_items += [
            "settings",
            # "reports",
            "help",
            "snippets",
            "explorer",
            "users",
        ]
    menu_items[:] = [
        item for item in menu_items if item.name not in hide_items
    ]


@hooks.register("register_icons")
def register_icons(icons):
    p = f"{settings.APPS_DIR}/templates/wagtailadmin/icons"
    icons += [f"wagtailadmin/icons/{item}" for item in os.listdir(p)]
    return icons


@hooks.register("construct_homepage_summary_items", order=1)
def register_summary_items(request, summary_items):
    summary_items.clear()
    summary_items.extend([i(request) for i in summary_items_to_append])
