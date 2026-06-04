from django.conf import settings


def set_jwt_cookies(response, access_token, refresh_token):
    cookie_opts = dict(
        httponly=True,
        secure=not settings.DEBUG,
        samesite='Lax',
    )
    response.set_cookie('access_token', str(access_token), max_age=15 * 60, **cookie_opts)
    response.set_cookie('refresh_token', str(refresh_token), max_age=7 * 24 * 60 * 60, **cookie_opts)
