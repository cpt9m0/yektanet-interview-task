from django.db import models
from django.utils.translation import ugettext_lazy as _


class ExpertArea(models.Model):
    name = models.CharField(_('name'), max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('expert area')
        verbose_name_plural = _('expert areas')
