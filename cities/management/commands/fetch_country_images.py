import os
import time
import requests
from django.core.management.base import BaseCommand, CommandParser
from cities.models import City, CountryImage

UNSPLASH_SEARCH_URL = "https://api.unsplash.com/search/photos"


class Command(BaseCommand):
    help = "Fetch hero images for countries (used on /country/<slug> pages) from Unsplash."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--force",
            action="store_true",
            help="Re-fetch images even for countries that already have one.",
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
        if not unsplash_key:
            self.stderr.write("UNSPLASH_ACCESS_KEY is not set in the environment.")
            return

        countries = sorted(City.objects.order_by().values_list("country", flat=True).distinct())
        total = len(countries)
        updated = skipped = failed = 0

        for idx, country in enumerate(countries, start=1):
            prefix = f"[{idx}/{total}] {country}"
            image = CountryImage.objects.filter(country=country).first()

            if image and image.image_url and not force:
                self.stdout.write(f"{prefix} → already set, skipping.")
                skipped += 1
                continue

            try:
                result = self._fetch_unsplash(country, unsplash_key)

                if not result:
                    self.stdout.write(self.style.WARNING(f"{prefix} → no image found, skipping."))
                    failed += 1
                    continue

                self.stdout.write(f"{prefix} → {result['url']}")

                if not dry_run:
                    CountryImage.objects.update_or_create(
                        country=country,
                        defaults={
                            "image_url": result["url"],
                            "attribution_name": result.get("attr_name", ""),
                            "attribution_url": result.get("attr_url", ""),
                        },
                    )

                updated += 1

            except Exception as e:
                self.stdout.write(self.style.WARNING(f"{prefix} → error: {e}"))
                failed += 1

            time.sleep(1)  # stay conservative — Unsplash free tier is 50 req/hour

        qualifier = " (dry run)" if dry_run else ""
        self.stdout.write(self.style.SUCCESS(
            f"\nDone{qualifier}. Updated: {updated}, Skipped: {skipped}, Failed: {failed}"
        ))

    def _fetch_unsplash(self, country: str, access_key: str) -> dict | None:
        params = {
            "query": country,
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
