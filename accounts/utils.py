import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import EmailVerificationToken

User = get_user_model()


def send_verification_email(user):
    token_obj = EmailVerificationToken.create_for_user(user)
    verify_url = f"{settings.FRONTEND_URL}/auth/verify-email?token={token_obj.token}"

    if not settings.DEBUG:
        send_via_mailer_function(
            name=user.username,
            email_to=user.email,
            message=(
                "Welcome to WeTravel! Click the link below to verify your email address "
                "and start exploring welcoming cities around the world.\n\n"
                f"{verify_url}\n\n"
                "This link expires in 24 hours. If you didn't create a WeTravel account, "
                "you can safely ignore this email."
            ),
        )
        return

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


def send_via_mailer_function(name, email_to, message):
    response = requests.post(
        settings.MAILER_FUNCTION_URL,
        json={'name': name, 'email_to': email_to, 'message': message},
        headers={'X-App-Secret-Key': settings.APP_SECRET_KEY},
        timeout=10,
    )
    response.raise_for_status()


def unique_username(base: str) -> str:
    username = base
    counter = 1
    while User.objects.filter(username=username).exists():
        username = f'{base}{counter}'
        counter += 1
    return username
