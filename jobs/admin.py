from django.contrib import admin

from jobs.models import OpportunityCategory, Opportunity, OpportunityRequest


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    pass


@admin.register(OpportunityCategory)
class OpportunityCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(OpportunityRequest)
class OpportunityRequestAdmin(admin.ModelAdmin):
    pass
