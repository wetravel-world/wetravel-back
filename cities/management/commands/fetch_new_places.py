import json
import os
import time
from pathlib import Path

import requests
from django.core.management.base import BaseCommand

from cities.models import City, Place


SEED_FILE = Path(__file__).resolve().parents[3] / 'new_places_seed.json'
TEXT_SEARCH_URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
PHOTO_URL = 'https://maps.googleapis.com/maps/api/place/photo'


class Command(BaseCommand):
    help = 'Seed places from new_places_seed.json; enrich with Google Places API if key is set'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be done without making changes',
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        api_key = os.environ.get('GOOGLE_PLACES_API_KEY') or ''

        if not api_key:
            self.stdout.write(self.style.WARNING(
                'GOOGLE_PLACES_API_KEY not set — places will be created without image/address/place_id'
            ))

        if not SEED_FILE.exists():
            self.stderr.write(self.style.ERROR(f'Seed file not found: {SEED_FILE}'))
            return

        with open(SEED_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)

        total = len(data)
        updated = skipped = 0

        for i, entry in enumerate(data, 1):
            slug = entry['city_slug']

            try:
                city = City.objects.get(slug=slug)
            except City.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'[{i}/{total}] SKIP — city not found: {slug}'))
                skipped += 1
                continue

            places = entry['places']

            if dry_run:
                self.stdout.write(
                    f'[{i}/{total}] DRY RUN — {city.name}: would delete {city.places.count()}, insert {len(places)}'
                )
                continue

            city.places.all().delete()

            for p in places:
                google_place_id = ''
                address = ''
                image_url = ''

                if api_key:
                    google_place_id, address, image_url = self._enrich(
                        p['name'], city.name, city.country, api_key
                    )
                    time.sleep(1)

                Place.objects.create(
                    city=city,
                    name=p['name'],
                    place_type=p['place_type'],
                    description=p['description'],
                    google_place_id=google_place_id,
                    address=address,
                    image_url=image_url,
                )
                self.stdout.write(
                    f'  + {p["name"]}'
                    + (f' — {address}' if address else '')
                    + (' [img]' if image_url else '')
                )

            self.stdout.write(f'[{i}/{total}] {city.name} — {len(places)} places saved')
            updated += 1

        if dry_run:
            self.stdout.write(self.style.SUCCESS('Dry run complete — no changes made'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Done. Updated: {updated}, Skipped: {skipped}'))

    def _enrich(self, name: str, city: str, country: str, api_key: str) -> tuple[str, str, str]:
        """Return (google_place_id, address, image_url) from a Text Search."""
        params = {
            'query': f'{name} {city} {country}',
            'key': api_key,
        }
        try:
            resp = requests.get(TEXT_SEARCH_URL, params=params, timeout=10)
            resp.raise_for_status()
            results = resp.json().get('results', [])
        except requests.RequestException as e:
            self.stderr.write(f'    Text Search failed for "{name}": {e}')
            return '', '', ''

        if not results:
            return '', '', ''

        result = results[0]
        place_id = result.get('place_id', '')
        address = result.get('formatted_address', '')
        image_url = self._fetch_photo(result, api_key)

        return place_id, address, image_url

    def _fetch_photo(self, result: dict, api_key: str) -> str:
        photos = result.get('photos', [])
        if not photos:
            return ''
        ref = photos[0].get('photo_reference', '')
        if not ref:
            return ''
        try:
            resp = requests.get(
                PHOTO_URL,
                params={'maxwidth': 800, 'photoreference': ref, 'key': api_key},
                timeout=10,
                allow_redirects=True,
            )
            resp.raise_for_status()
            return resp.url
        except requests.RequestException as e:
            self.stderr.write(f'    Photo fetch failed: {e}')
            return ''
