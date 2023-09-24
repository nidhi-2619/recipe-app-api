"""
Django admin customization
"""


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _("Permissions"),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),

    ]


class RecipeAdmin(admin.ModelAdmin):
    """Customising recipe admin  to display other fields"""
    list_display = ('title', 'price', 'time_minutes')

    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True


class IngredientAdmin(admin.ModelAdmin):
    """Customising ingredient admin to display other fields."""
    list_display = ('name', 'user')

    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Ingredient, IngredientAdmin)