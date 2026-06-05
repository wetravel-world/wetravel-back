from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import EmailVerificationToken

User = get_user_model()


def send_verification_email(user):
    token_obj = EmailVerificationToken.create_for_user(user)
    verify_url = f"{settings.FRONTEND_URL}/auth/verify-email?token={token_obj.token}"
    html = render_to_string('email/verify_email.html', {
        'username': user.username,
        'verify_url': verify_url,
        'frontend_url': settings.FRONTEND_URL,
    })
    send_mail(
        subject='Confirm your WeTravel email',
        message=f"Hi {user.username},\n\nVerify your email: {verify_url}\n\nThis link expires in 24 hours.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        html_message=html,
        fail_silently=False,
    )


def unique_username(base: str) -> str:
    username = base
    counter = 1
    while User.objects.filter(username=username).exists():
        username = f'{base}{counter}'
        counter += 1
    return username
