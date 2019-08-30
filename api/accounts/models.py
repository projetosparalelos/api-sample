from core.models import LanguageModel, UUIDModel
from core.time_zones import TIME_ZONES_CHOICES
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, UUIDModel, LanguageModel):
    IOS = 'ios'
    ANDROID = 'android'
    PLATFORM_CHOICES = (
        (IOS, _("iOS")),
        (ANDROID, _("Android"))
    )

    email = models.EmailField(unique=True, db_index=True, max_length=96, verbose_name=_("email"))
    full_name = models.CharField(db_index=True, max_length=128, verbose_name=_("full name"))
    username = models.CharField(unique=True, db_index=True, max_length=32, verbose_name=_("username"))
    is_active = models.BooleanField(db_index=True, default=True, verbose_name=_("is active"))
    is_premium = models.BooleanField(db_index=True, default=False, verbose_name=_("is premium"))
    is_staff = models.BooleanField(db_index=True, default=False, verbose_name=_("is staff"))
    time_zone = models.CharField(db_index=True, max_length=64, choices=TIME_ZONES_CHOICES, verbose_name=_("time zone"))
    emails_subscribed = models.BooleanField(db_index=True, default=True, verbose_name=_("emails: subscribed"))
    emails_bounced = models.DateTimeField(db_index=True, blank=True, null=True, verbose_name=_("emails: bounced"))
    emails_complained = models.DateTimeField(db_index=True, blank=True, null=True,
                                             verbose_name=_("emails: complained"))
    platform = models.CharField(max_length=16, blank=True, choices=PLATFORM_CHOICES, verbose_name=_("platform"))
    jwt_secret_key = models.CharField(max_length=2048, verbose_name=_("JWT secret key"))

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'full_name', 'language', 'time_zone']

    objects = UserManager()

    class Meta:
        ordering = ['-created']
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.full_name
    get_full_name.short_description = _("full name")

    def get_short_name(self):
        return self.full_name.split()[0]
    get_short_name.short_description = _("name")

    @property
    def now(self):
        kwargs = {}
        if self.time_zone:
            kwargs.update(timezone=timezone.pytz.timezone(self.time_zone))
        return timezone.localtime(**kwargs)
