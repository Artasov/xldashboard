# app/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        *BaseUserAdmin.fieldsets,
        (
            _('Дополнительная информация'),
            {
                'fields': ('phone',),
            },
        ),
    )
    add_fieldsets = (
        *BaseUserAdmin.add_fieldsets,
        (
            _('Дополнительная информация'),
            {
                'fields': ('phone',),
            },
        ),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone')
    ordering = ('username',)


@admin.register(User)
class UserAdmin(CustomUserAdmin):
    pass
