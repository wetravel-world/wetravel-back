from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('WeTravel', {'fields': ('avatar_url', 'is_google_auth')}),
    )
    list_display = ('username', 'email', 'is_google_auth', 'is_staff')
