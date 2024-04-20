from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from {{ cookiecutter.project_slug }}.users.forms import UserAdminChangeForm, UserAdminCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name","last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["email", "name", "phone_number","group_names"]
    search_fields = ["name"]
    list_filter = ("groups",)
    ordering = ["email"]

    def group_names(self, instance):
        return instance.group_names

    group_names.short_description = "groups"
