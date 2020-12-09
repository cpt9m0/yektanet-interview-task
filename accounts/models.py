from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from accounts.managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), blank=False, null=False, unique=True)
    is_employer = models.BooleanField(_('employer'), blank=False, null=False, default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['is_employer',]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return str(self.email)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

    class Meta:
        abstract = True


class UserProfile(Profile):
    gender_choices = (
        ('male', _('Male')),
        ('female', _('Female')),
    )
    age = models.PositiveIntegerField(_('age'), blank=True, null=True)
    gender = models.CharField(_('gender'), max_length=6, choices=gender_choices)

    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')


class EmployerProfile(Profile):
    company_name = models.CharField(_('company name'), max_length=128, blank=True, null=True)
    company_address = models.CharField(_('company address'), max_length=1024, blank=True, null=True)
    company_phone = models.CharField(_('company phone'), max_length=12, blank=True, null=True)
    established_year = models.PositiveIntegerField(_('established year'), blank=True, null=True)

    class Meta:
        verbose_name = _('employer profile')
        verbose_name_plural = _('employer profiles')
