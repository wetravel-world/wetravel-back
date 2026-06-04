from django.db import migrations


CITIES = [
    {
        "name": "Marrakech",
        "country": "Morocco",
        "continent": "Africa",
        "slug": "marrakech-morocco",
        "description": (
            "Marrakech is Morocco's most visited city, a sensory overload of spice markets, "
            "riads, and the vast Djemaa el-Fna square. As an African city with a majority "
            "Black and Amazigh population, Black travelers from the diaspora often find "
            "Marrakech more relaxed than European destinations. Interactions are generally "
            "warm, though persistent vendor attention in the medina affects all tourists equally."
        ),
        "welcome_score": 7.5,
        "latitude": 31.628700,
        "longitude": -7.992900,
        "meta_description": "Is Marrakech welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Kingston",
        "country": "Jamaica",
        "continent": "Americas",
        "slug": "kingston-jamaica",
        "description": (
            "Kingston is the cultural capital of Jamaica and the birthplace of reggae, dancehall, "
            "and ska. As a predominantly Black city, it offers an instantly affirming environment "
            "for African diaspora travelers seeking cultural connection. The Bob Marley Museum, "
            "National Gallery, and vibrant street food scene make it a rich destination, though "
            "visitors should stay aware of neighborhood safety as in any major city."
        ),
        "welcome_score": 8.5,
        "latitude": 17.997100,
        "longitude": -76.793600,
        "meta_description": "Is Kingston welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Montreal",
        "country": "Canada",
        "continent": "Americas",
        "slug": "montreal-canada",
        "description": (
            "Montreal is Canada's most culturally vibrant city — bilingual, cosmopolitan, and "
            "home to a large Haitian and Afro-Caribbean diaspora community, particularly in the "
            "Little Burgundy and Côte-des-Neiges neighborhoods. Black travelers consistently "
            "rate Montreal as one of North America's most welcoming cities, with a thriving "
            "Black arts scene, great food, and a genuinely diverse urban culture."
        ),
        "welcome_score": 8.0,
        "latitude": 45.501700,
        "longitude": -73.567300,
        "meta_description": "Is Montreal welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Atlanta",
        "country": "United States",
        "continent": "Americas",
        "slug": "atlanta-united-states",
        "description": (
            "Atlanta is widely known as the Black Mecca of the South — home to HBCUs, "
            "Black-owned businesses, influential civil rights history, and one of the highest "
            "concentrations of Black wealth and culture in the US. The city is a natural hub "
            "for African American travelers and diaspora visitors alike, offering exceptional "
            "representation, hospitality, and community."
        ),
        "welcome_score": 9.0,
        "latitude": 33.749000,
        "longitude": -84.388000,
        "meta_description": "Is Atlanta welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "New Orleans",
        "country": "United States",
        "continent": "Americas",
        "slug": "new-orleans-united-states",
        "description": (
            "New Orleans is one of the most culturally unique cities in America, shaped "
            "profoundly by African, Caribbean, and Creole heritage. Jazz, second-line parades, "
            "and Mardi Gras all have deep Black roots. Black travelers consistently rate "
            "New Orleans as a top destination, with exceptional food, music, and a community "
            "that takes visible pride in its African American history."
        ),
        "welcome_score": 8.5,
        "latitude": 29.951100,
        "longitude": -90.071500,
        "meta_description": "Is New Orleans welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Bahia",
        "country": "Brazil",
        "continent": "Americas",
        "slug": "bahia-brazil",
        "description": (
            "Bahia — centered on Salvador da Bahia — is often called the most African city "
            "outside of Africa, with over 80% of its population of African descent. The city's "
            "culture, cuisine, music, and Candomblé religion are deeply rooted in West African "
            "traditions. For Black travelers, Bahia offers a rare experience of profound cultural "
            "belonging, expressed through Carnaval, capoeira, and acarajé on every street corner."
        ),
        "welcome_score": 8.5,
        "latitude": -12.971400,
        "longitude": -38.501400,
        "meta_description": "Is Bahia welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Cartagena",
        "country": "Colombia",
        "continent": "Americas",
        "slug": "cartagena-colombia",
        "description": (
            "Cartagena is a UNESCO-listed colonial port city on Colombia's Caribbean coast, "
            "with a majority Afro-Colombian population. The city's Getsemaní neighborhood "
            "pulses with Afro-Caribbean culture, cumbia, and street art. Black travelers "
            "from North America and the Caribbean consistently cite Cartagena as one of the "
            "most welcoming cities in Latin America, with a deep sense of shared cultural identity."
        ),
        "welcome_score": 8.0,
        "latitude": 10.391000,
        "longitude": -75.479400,
        "meta_description": "Is Cartagena welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Dubai",
        "country": "United Arab Emirates",
        "continent": "Middle East",
        "slug": "dubai-united-arab-emirates",
        "description": (
            "Dubai is one of the world's most internationally connected cities, drawing visitors "
            "from across Africa, South Asia, and the West. It is extremely safe and tourist-friendly, "
            "with world-class infrastructure and service. Black travelers report broadly positive "
            "experiences in tourist areas, though colorism in hiring and service has been documented, "
            "and LGBTQ+ travelers or those not conforming to local customs should exercise caution."
        ),
        "welcome_score": 6.5,
        "latitude": 25.204800,
        "longitude": 55.270800,
        "meta_description": "Is Dubai welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Singapore",
        "country": "Singapore",
        "continent": "Asia",
        "slug": "singapore-singapore",
        "description": (
            "Singapore is one of the safest and most efficient cities in the world, with a "
            "multiracial society built on Chinese, Malay, and Indian communities. It is highly "
            "international, with a strong expat presence, and Black travelers report largely "
            "incident-free, comfortable stays. The country's strict rule of law means "
            "discrimination is rarely overt, though Black travelers note Singapore lacks "
            "significant African diaspora cultural touchpoints."
        ),
        "welcome_score": 7.5,
        "latitude": 1.352100,
        "longitude": 103.819800,
        "meta_description": "Is Singapore welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Amsterdam",
        "country": "Netherlands",
        "continent": "Europe",
        "slug": "amsterdam-netherlands",
        "description": (
            "Amsterdam is one of Europe's most liberal and open cities, with a vibrant "
            "Surinamese and Antillean community that has shaped the city's food, music, and "
            "culture for generations. Neighborhoods like Bijlmer are hubs of Afro-Dutch life. "
            "Black travelers rate Amsterdam highly for its openness and diversity, though "
            "the country's annual Sinterklaas controversy signals ongoing cultural tensions "
            "around race that travellers should be aware of."
        ),
        "welcome_score": 7.5,
        "latitude": 52.370200,
        "longitude": 4.895200,
        "meta_description": "Is Amsterdam welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
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
                "score_count": 0,
                "latitude": data["latitude"],
                "longitude": data["longitude"],
                "hero_image_url": "",
                "meta_description": data["meta_description"],
            },
        )


def unseed_cities(apps, schema_editor):
    City = apps.get_model("cities", "City")
    new_slugs = [
        "marrakech-morocco",
        "kingston-jamaica",
        "montreal-canada",
        "bahia-brazil",
        "cartagena-colombia",
        "dubai-united-arab-emirates",
        "singapore-singapore",
        "amsterdam-netherlands",
    ]
    City.objects.filter(slug__in=new_slugs).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("cities", "0007_add_comment_reply"),
    ]

    operations = [
        migrations.RunPython(seed_cities, reverse_code=unseed_cities),
    ]
