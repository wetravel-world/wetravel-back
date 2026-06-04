import time
import os
import requests
from django.core.management.base import BaseCommand
from cities.models import City, Place


PLACES_API_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
PLACE_DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"
PHOTO_URL = "https://maps.googleapis.com/maps/api/place/photo"

PLACE_TYPE_MAP = {
    "museum": "museum",
    "art_gallery": "art gallery",
    "park": "park",
    "tourist_attraction": "tourist attraction",
    "church": "church",
    "mosque": "mosque",
    "hindu_temple": "temple",
    "amusement_park": "amusement park",
    "zoo": "zoo",
    "aquarium": "aquarium",
    "stadium": "stadium",
    "restaurant": "restaurant",
    "night_club": "nightclub",
    "shopping_mall": "shopping mall",
}


def resolve_place_type(types: list[str]) -> str:
    for t in types:
        if t in PLACE_TYPE_MAP:
            return PLACE_TYPE_MAP[t]
    return "tourist attraction"


class Command(BaseCommand):
    help = "Fetch top tourist attractions for each city via Google Places API and save as Place objects."

    def handle(self, *args, **options):
        api_key = os.environ.get("GOOGLE_PLACES_API_KEY")
        if not api_key:
            self.stderr.write("GOOGLE_PLACES_API_KEY is not set in the environment.")
            return

        cities = City.objects.all()
        self.stdout.write(f"Processing {cities.count()} cities...")

        for city in cities:
            existing_count = city.places.count()
            if existing_count >= 5:
                self.stdout.write(f"  Skipping {city.name} — already has {existing_count} places.")
                continue

            self.stdout.write(f"  Fetching places for {city.name}, {city.country}...")
            self._fetch_places_for_city(city, api_key)
            time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Done."))

    def _fetch_places_for_city(self, city: City, api_key: str) -> None:
        params = {
            "location": f"{city.latitude},{city.longitude}",
            "radius": 10000,
            "type": "tourist_attraction",
            "rankby": "prominence",
            "key": api_key,
        }

        try:
            response = requests.get(PLACES_API_URL, params=params, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            self.stderr.write(f"    Nearby Search failed for {city.name}: {e}")
            return

        data = response.json()
        results = data.get("results", [])

        if not results:
            self.stdout.write(f"    No results returned for {city.name}.")
            return

        saved = 0
        for result in results:
            if saved >= 5:
                break

            place_id = result.get("place_id", "")
            name = result.get("name", "")

            if Place.objects.filter(google_place_id=place_id).exists():
                continue

            address = result.get("vicinity", "")
            types = result.get("types", [])
            place_type = resolve_place_type(types)

            description = self._fetch_editorial_summary(place_id, api_key)
            time.sleep(1)

            image_url = self._fetch_photo_url(result, api_key)

            Place.objects.create(
                city=city,
                name=name,
                description=description,
                place_type=place_type,
                google_place_id=place_id,
                address=address,
                image_url=image_url or "",
            )
            saved += 1
            self.stdout.write(f"    Saved: {name}")

        self.stdout.write(f"    {saved} places saved for {city.name}.")

    def _fetch_editorial_summary(self, place_id: str, api_key: str) -> str:
        params = {
            "place_id": place_id,
            "fields": "editorial_summary,name",
            "key": api_key,
        }
        try:
            response = requests.get(PLACE_DETAILS_URL, params=params, timeout=10)
            response.raise_for_status()
            detail = response.json().get("result", {})
            summary = detail.get("editorial_summary", {}).get("overview", "")
            return summary
        except requests.RequestException as e:
            self.stderr.write(f"      Place Details failed for {place_id}: {e}")
            return ""

    def _fetch_photo_url(self, result: dict, api_key: str) -> str:
        photos = result.get("photos", [])
        if not photos:
            return ""

        photo_reference = photos[0].get("photo_reference", "")
        if not photo_reference:
            return ""

        # Build a direct URL — this redirects to the actual image.
        # We follow the redirect to capture the final CDN URL for storage.
        params = {
            "maxwidth": 800,
            "photoreference": photo_reference,
            "key": api_key,
        }
        try:
            response = requests.get(PHOTO_URL, params=params, timeout=10, allow_redirects=True)
            response.raise_for_status()
            return response.url
        except requests.RequestException as e:
            self.stderr.write(f"      Photo fetch failed: {e}")
            return ""
