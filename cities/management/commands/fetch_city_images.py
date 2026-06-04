import os
import time
import requests
from django.core.management.base import BaseCommand, CommandParser
from cities.models import City

UNSPLASH_SEARCH_URL = "https://api.unsplash.com/search/photos"
PLACES_TEXT_SEARCH_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
PLACE_DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"
PLACES_PHOTO_URL = "https://maps.googleapis.com/maps/api/place/photo"


class Command(BaseCommand):
    help = "Fetch hero images for cities from Unsplash (with Google Places fallback)."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--force",
            action="store_true",
            help="Re-fetch images even for cities that already have one.",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Log what would be fetched without saving anything.",
        )

    def handle(self, *args, **options) -> None:
        force = options["force"]
        dry_run = options["dry_run"]

        unsplash_key = os.environ.get("UNSPLASH_ACCESS_KEY")
        google_key = os.environ.get("GOOGLE_PLACES_API_KEY")

        if not unsplash_key:
            self.stderr.write("UNSPLASH_ACCESS_KEY is not set in the environment.")
            return

        cities = City.objects.all().order_by("name")
        total = cities.count()
        updated = skipped = failed = 0

        for idx, city in enumerate(cities, start=1):
            prefix = f"[{idx}/{total}] {city.name}, {city.country}"

            if city.hero_image_url and not force:
                self.stdout.write(f"{prefix} → already set, skipping.")
                skipped += 1
                continue

            try:
                result = self._fetch_unsplash(city, unsplash_key)
                source = "unsplash"

                if not result and google_key:
                    result = self._fetch_google_fallback(city, google_key)
                    source = "google"
                    time.sleep(1)

                if not result:
                    self.stdout.write(self.style.WARNING(f"{prefix} → no image found, skipping."))
                    failed += 1
                    continue

                image_url = result["url"]
                attr_name = result.get("attr_name", "")
                attr_url = result.get("attr_url", "")

                self.stdout.write(f"{prefix} → [{source}] {image_url}")

                if not dry_run:
                    city.hero_image_url = image_url
                    city.hero_image_attribution_name = attr_name
                    city.hero_image_attribution_url = attr_url
                    city.save(update_fields=[
                        "hero_image_url",
                        "hero_image_attribution_name",
                        "hero_image_attribution_url",
                    ])

                updated += 1

            except Exception as e:
                self.stdout.write(self.style.WARNING(f"{prefix} → error: {e}"))
                failed += 1

            time.sleep(1)

        qualifier = " (dry run)" if dry_run else ""
        self.stdout.write(self.style.SUCCESS(
            f"\nDone{qualifier}. Updated: {updated}, Skipped: {skipped}, Failed: {failed}"
        ))

    def _fetch_unsplash(self, city: City, access_key: str) -> dict | None:
        params = {
            "query": f"{city.name} {city.country}",
            "per_page": 1,
            "orientation": "landscape",
        }
        headers = {"Authorization": f"Client-ID {access_key}"}

        response = requests.get(UNSPLASH_SEARCH_URL, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        results = response.json().get("results", [])

        if not results:
            return None

        photo = results[0]
        return {
            "url": photo["urls"]["regular"],
            "attr_name": photo["user"]["name"],
            "attr_url": photo["user"]["links"]["html"],
        }

    def _fetch_google_fallback(self, city: City, api_key: str) -> dict | None:
        # Step 1: text search to get a place_id
        search_params = {
            "query": f"{city.name} {city.country}",
            "key": api_key,
        }
        search_resp = requests.get(PLACES_TEXT_SEARCH_URL, params=search_params, timeout=10)
        search_resp.raise_for_status()
        search_results = search_resp.json().get("results", [])

        if not search_results:
            return None

        place_id = search_results[0].get("place_id")
        if not place_id:
            return None

        time.sleep(1)

        # Step 2: place details to get photo reference
        details_params = {
            "place_id": place_id,
            "fields": "photos",
            "key": api_key,
        }
        details_resp = requests.get(PLACE_DETAILS_URL, params=details_params, timeout=10)
        details_resp.raise_for_status()
        photos = details_resp.json().get("result", {}).get("photos", [])

        if not photos:
            return None

        photo_ref = photos[0].get("photo_reference")
        if not photo_ref:
            return None

        time.sleep(1)

        # Step 3: follow redirect to get final CDN URL
        photo_params = {
            "maxwidth": 1200,
            "photoreference": photo_ref,
            "key": api_key,
        }
        photo_resp = requests.get(PLACES_PHOTO_URL, params=photo_params, timeout=10, allow_redirects=True)
        photo_resp.raise_for_status()

        return {"url": photo_resp.url, "attr_name": "", "attr_url": ""}
