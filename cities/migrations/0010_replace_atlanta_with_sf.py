from django.db import migrations


SF = {
    "name": "San Francisco",
    "country": "United States",
    "continent": "Americas",
    "slug": "san-francisco-united-states",
    "description": (
        "San Francisco is one of the United States' most progressive cities, long shaped "
        "by civil rights activism and Black community leadership in the Fillmore District, "
        "historically known as the 'Harlem of the West.' Tech-era gentrification has "
        "dramatically displaced the city's Black population — from over 13% in the 1970s "
        "to around 5% today — hollowing out the very neighborhoods that gave the city its "
        "reputation. Black travelers find a welcoming, politically aware environment, "
        "though the steep cost of living and loss of historic Black spaces are real and visible."
    ),
    "welcome_score": 7.5,
    "latitude": 37.774900,
    "longitude": -122.419400,
    "meta_description": (
        "Is San Francisco welcoming for Black travelers? "
        "Read reviews, get the welcome score, find places to visit."
    ),
}

ATLANTA_SLUG = "atlanta-united-states"


def forward(apps, schema_editor):
    City = apps.get_model("cities", "City")
    City.objects.filter(slug=ATLANTA_SLUG).delete()
    City.objects.create(
        name=SF["name"],
        country=SF["country"],
        continent=SF["continent"],
        slug=SF["slug"],
        description=SF["description"],
        welcome_score=SF["welcome_score"],
        score_count=0,
        latitude=SF["latitude"],
        longitude=SF["longitude"],
        hero_image_url="",
        meta_description=SF["meta_description"],
    )


def backward(apps, schema_editor):
    City = apps.get_model("cities", "City")
    City.objects.filter(slug=SF["slug"]).delete()
    City.objects.create(
        name="Atlanta",
        country="United States",
        continent="Americas",
        slug=ATLANTA_SLUG,
        description=(
            "Atlanta is widely known as the Black Mecca of the South — home to HBCUs, "
            "Black-owned businesses, influential civil rights history, and one of the highest "
            "concentrations of Black wealth and culture in the US. The city is a natural hub "
            "for African American travelers and diaspora visitors alike, offering exceptional "
            "representation, hospitality, and community."
        ),
        welcome_score=9.0,
        score_count=0,
        latitude=33.749000,
        longitude=-84.388000,
        hero_image_url="",
        meta_description=(
            "Is Atlanta welcoming for Black travelers? "
            "Read reviews, get the welcome score, find places to visit."
        ),
    )


class Migration(migrations.Migration):

    dependencies = [
        ("cities", "0009_alter_city_options"),
    ]

    operations = [
        migrations.RunPython(forward, reverse_code=backward),
    ]
