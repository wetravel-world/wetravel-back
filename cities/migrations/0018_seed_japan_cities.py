from django.db import migrations


CITIES = [
    {
        "name": "Tokyo",
        "country": "Japan",
        "continent": "Asia",
        "slug": "tokyo-japan",
        "description": (
            "Tokyo is one of the world's largest and safest cities, known for its "
            "efficiency, cleanliness, and blend of ultramodern and traditional culture. "
            "Black travelers generally report feeling physically safe and rarely encounter "
            "hostility, though curiosity, staring, and occasional 'Japanese only' "
            "establishments have been documented. The city's small but growing African "
            "and Caribbean diaspora is concentrated in areas like Roppongi and Shin-Okubo."
        ),
        "welcome_score": 7.0,
        "latitude": 35.676200,
        "longitude": 139.650300,
        "meta_description": "Is Tokyo welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Osaka",
        "country": "Japan",
        "continent": "Asia",
        "slug": "osaka-japan",
        "description": (
            "Osaka is Japan's culinary capital and its most laid-back major city, known "
            "for street food, nightlife, and a friendlier, more outgoing local culture than "
            "Tokyo. Black travelers often describe Osaka as approachable and fun, though, as "
            "elsewhere in Japan, isolated reports of entry refusals at certain bars and clubs "
            "persist. Visible diversity is limited outside of tourist and nightlife districts "
            "like Dotonbori and Namba."
        ),
        "welcome_score": 7.0,
        "latitude": 34.693700,
        "longitude": 135.502300,
        "meta_description": "Is Osaka welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Kyoto",
        "country": "Japan",
        "continent": "Asia",
        "slug": "kyoto-japan",
        "description": (
            "Kyoto is Japan's former imperial capital, famous for its temples, shrines, "
            "and preserved geisha districts. It is calm, walkable, and considered very safe, "
            "though it is far less internationally diverse than Tokyo or Osaka and Black "
            "visitors are likely to draw curious looks, especially outside central tourist "
            "areas. Most travelers report respectful, if reserved, interactions overall."
        ),
        "welcome_score": 6.5,
        "latitude": 35.011600,
        "longitude": 135.768100,
        "meta_description": "Is Kyoto welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Fukuoka",
        "country": "Japan",
        "continent": "Asia",
        "slug": "fukuoka-japan",
        "description": (
            "Fukuoka is a compact, fast-growing city on the southern island of Kyushu, "
            "known for its food stalls (yatai), beaches, and relaxed pace compared to Tokyo "
            "or Osaka. It sees far fewer foreign tourists, so Black travelers should expect "
            "more staring and a smaller expat or diaspora presence, but reports of overt "
            "hostility are rare and locals are generally described as polite and curious "
            "rather than unwelcoming."
        ),
        "welcome_score": 6.5,
        "latitude": 33.590400,
        "longitude": 130.401700,
        "meta_description": "Is Fukuoka welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
]


def seed_cities(apps, schema_editor):
    City = apps.get_model("cities", "City")
    for data in CITIES:
        City.objects.get_or_create(
            slug=data["slug"],
            defaults={
                "name": data["name"],
                "country": data["country"],
                "continent": data["continent"],
                "description": data["description"],
                "welcome_score": data["welcome_score"],
                "base_score": data["welcome_score"],
                "score_count": 0,
                "latitude": data["latitude"],
                "longitude": data["longitude"],
                "hero_image_url": "",
                "meta_description": data["meta_description"],
            },
        )


def unseed_cities(apps, schema_editor):
    City = apps.get_model("cities", "City")
    new_slugs = [city["slug"] for city in CITIES]
    City.objects.filter(slug__in=new_slugs).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("cities", "0017_seed_city_descriptions_fr"),
    ]

    operations = [
        migrations.RunPython(seed_cities, reverse_code=unseed_cities),
    ]
