from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    ordering = ['-date_joined']
    list_display = [
        'short_id',
        'email',
        'name',
        'is_staff',
        'is_active',
        'colored_status',
        'date_joined'
    ]

    list_filter = [
        'is_staff',
        'is_active',
        'is_superuser',
        'date_joined'
    ]

    search_fields = ['email', 'name']
    readonly_fields = ['id', 'date_joined', 'updated_time', 'last_login']

    fieldsets = (
        ("Login Info", {
            'fields': ('email', 'password')
        }),

        ("Personal Information", {
            'fields': ('name',)
        }),

        ("Permissions & Access Control", {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            )
        }),

        ("Important Dates", {
            'fields': (
                'last_login',
                'date_joined',
                'updated_time'
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'name',
                'password1',
                'password2',
                'is_staff',
                'is_active'
            ),
        }),
    )

    actions = ['activate_users', 'deactivate_users']

    # ---------- Custom Methods ----------

    def short_id(self, obj):
        return str(obj.id)[:8]
    short_id.short_description = "User ID"

    def colored_status(self, obj):
        if obj.is_active:
            return format_html('<span style="color: green; font-weight: bold;">Active</span>')
        return format_html('<span style="color: red; font-weight: bold;">Inactive</span>')
    colored_status.short_description = "Status"

    # ---------- Bulk Actions ----------

    def activate_users(self, request, queryset):
        queryset.update(is_active=True)
    activate_users.short_description = "Activate selected users"

    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_users.short_description = "Deactivate selected users"
