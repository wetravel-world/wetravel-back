import random
import urllib.parse

from django.contrib.auth.models import AbstractUser
from django.db import models

from .constant import _AVATAR_COLORS


def _generate_avatar_url(username: str) -> str:
    color = random.choice(_AVATAR_COLORS)
    name = urllib.parse.quote(username)
    return (
        f"https://ui-avatars.com/api/"
        f"?name={name}&background={color}&color=fff&size=200&bold=true"
    )


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='email address')
    avatar_url = models.URLField(blank=True)
    is_google_auth = models.BooleanField(default=False)

    class Meta:
        db_table = 'accounts_user'

    def save(self, *args, **kwargs):
        if not self.pk and not self.avatar_url and self.username:
            self.avatar_url = _generate_avatar_url(self.username)
        super().save(*args, **kwargs)
