from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.utils.translation import ugettext_lazy as _

from accounts.models import User, UserProfile, EmployerProfile, ExpertArea


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_employer', 'is_staff', 'is_superuser', 'groups', 'user_permissions',),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'is_employer',)
    list_filter = ('is_staff', 'is_employer', 'is_superuser', 'is_active', 'groups',)
    search_fields = ('email',)
    ordering = ('email',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(EmployerProfile)
class EmployerProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(ExpertArea)
class ExpertAreaAdmin(admin.ModelAdmin):
    pass
