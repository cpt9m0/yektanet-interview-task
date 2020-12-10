from django.contrib import admin

from jobs.models import ExpertArea


@admin.register(ExpertArea)
class ExpertAreaAdmin(admin.ModelAdmin):
    pass
