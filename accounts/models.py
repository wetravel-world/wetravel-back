import secrets
from datetime import timedelta

from django.conf import settings
from django.db import models
from django.utils import timezone

from users.models import User  # noqa: F401 – re-exported so existing migrations resolve

TOKEN_EXPIRY_HOURS = 24


class EmailVerificationToken(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='email_verification_token',
    )
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'accounts_email_verification_token'

    @classmethod
    def create_for_user(cls, user):
        cls.objects.filter(user=user).delete()
        return cls.objects.create(user=user, token=secrets.token_urlsafe(32))

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(hours=TOKEN_EXPIRY_HOURS)
