from django.contrib import admin
from apps.accounts.models import User, Address
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.accounts.form import CreateUserForm, UserChangeForm


class AddressInline(admin.TabularInline):
    model = Address
    extra = 0


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = CreateUserForm

    list_display = ("email", "phone", "username", "is_staff")
    list_filter = ("username", "is_staff", "is_active", "is_superuser")
    readonly_fields = ("last_login",)

    fieldsets = (
        (
            "Main",
            {
                "fields": (
                    "email",
                    "phone",
                    "username",
                    "password",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_superuser",
                    "last_login",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "phone",
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "username",
                )
            },
        ),
    )

    search_fields = ("email", "username", "first_name", "last_name")
    ordering = ("username",)
    filter_horizontal = ("groups", "user_permissions")
    inlines = (AddressInline,)
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     is_superuser = request.user.is_superuser
    #     if not is_superuser:
    #         form.base_fields['is_superuser'].disabled = True
    #     return form


admin.site.register(User, UserAdmin)
