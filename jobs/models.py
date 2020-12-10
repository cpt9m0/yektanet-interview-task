from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.models import EmployerProfile, UserProfile


class OpportunityCategory(models.Model):
    name = models.CharField(_('name'), max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('opportunity category')
        verbose_name_plural = _('opportunity categories')


class Opportunity(models.Model):
    employer = models.ForeignKey(to=EmployerProfile, on_delete=models.CASCADE, verbose_name=_('employer'))
    title = models.CharField(_('title'), max_length=128)
    description = models.TextField(_('description'), blank=True, null=True)
    image = models.FileField(_('image'), upload_to='opportunities/', blank=True, null=True)
    salary = models.PositiveBigIntegerField(_('salary'), blank=True, null=True)
    working_hours = models.IntegerField(_('working hours'), blank=True, null=True)
    category = models.ManyToManyField(to=OpportunityCategory, related_name='opportunities', verbose_name=_('category'))

    expiration_date = models.DateTimeField(_('expiration date'), blank=True, null=True)
    posted_date = models.DateTimeField(_('posted date'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('opportunity')
        verbose_name_plural = _('opportunities')


class OpportunityRequest(models.Model):
    opportunity = models.ForeignKey(to=Opportunity, on_delete=models.CASCADE, verbose_name=_('opportunity'))
    user = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, verbose_name=_('user'))

    request_date = models.DateTimeField(verbose_name=_('requested at'), auto_now_add=True)

    def __str__(self):
        return f"{self.user} for {self.opportunity}"

    class Meta:
        verbose_name = _('Opportunity Request')
        verbose_name_plural = _('Opportunity Requests')
