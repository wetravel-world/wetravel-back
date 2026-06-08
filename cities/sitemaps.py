from urllib.parse import urlparse

from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.utils.text import slugify

from .models import City


class CitySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return City.objects.order_by('-updated_at')

    def location(self, obj):
        return f'/city/{obj.slug}/'

    def lastmod(self, obj):
        return obj.updated_at

    def get_urls(self, page=1, site=None, protocol=None):
        parsed = urlparse(settings.FRONTEND_URL)

        class _FrontendSite:
            domain = parsed.netloc
            name = parsed.netloc

        return super().get_urls(page=page, site=_FrontendSite(), protocol=parsed.scheme)


class CountrySitemap(Sitemap):
    """Country overview pages (`/country/<slug>`).

    There's no Country model — `country` is a plain field on City — so, like
    CountryDetailView, the slug is derived by slugifying each distinct country name.
    """
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return City.objects.values_list('country', flat=True).distinct().order_by('country')

    def location(self, country):
        return f'/country/{slugify(country)}/'

    def get_urls(self, page=1, site=None, protocol=None):
        parsed = urlparse(settings.FRONTEND_URL)

        class _FrontendSite:
            domain = parsed.netloc
            name = parsed.netloc

        return super().get_urls(page=page, site=_FrontendSite(), protocol=parsed.scheme)


class StaticPagesSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    _pages = [
        ('/', 1.0),
        ('/search', 0.8),
    ]

    def items(self):
        return self._pages

    def location(self, item):
        return item[0]

    def priority(self, item):
        return item[1]

    def get_urls(self, page=1, site=None, protocol=None):
        parsed = urlparse(settings.FRONTEND_URL)

        class _FrontendSite:
            domain = parsed.netloc
            name = parsed.netloc

        return super().get_urls(page=page, site=_FrontendSite(), protocol=parsed.scheme)
