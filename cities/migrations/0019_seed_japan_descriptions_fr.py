# Hand-authored French translations of City.description / meta_description
# for the Japan cities seeded in 0018 (added after 0017 ran, so they were
# missed by the original translation seed).

from django.db import migrations

DESCRIPTIONS_FR = {
    "tokyo-japan": (
        "Tokyo est l'une des plus grandes et des plus sûres villes du monde, connue pour "
        "son efficacité, sa propreté et son mélange de culture ultramoderne et "
        "traditionnelle. Les voyageurs noirs s'y sentent généralement en sécurité et "
        "rencontrent rarement de l'hostilité, bien que la curiosité, les regards insistants "
        "et certains établissements « réservés aux Japonais » aient été documentés. La "
        "petite mais croissante diaspora africaine et caribéenne se concentre dans des "
        "quartiers comme Roppongi et Shin-Okubo."
    ),
    "osaka-japan": (
        "Osaka est la capitale culinaire du Japon et sa plus grande ville la plus "
        "décontractée, connue pour sa street food, sa vie nocturne et une culture locale "
        "plus chaleureuse et expansive qu'à Tokyo. Les voyageurs noirs décrivent souvent "
        "Osaka comme accessible et conviviale, bien que, comme ailleurs au Japon, des refus "
        "d'entrée isolés dans certains bars et clubs persistent. La diversité visible reste "
        "limitée en dehors des quartiers touristiques et nocturnes comme Dotonbori et Namba."
    ),
    "kyoto-japan": (
        "Kyoto est l'ancienne capitale impériale du Japon, célèbre pour ses temples, ses "
        "sanctuaires et ses quartiers de geishas préservés. Elle est calme, facile à "
        "parcourir à pied et considérée comme très sûre, mais elle est bien moins "
        "internationalement diverse que Tokyo ou Osaka, et les visiteurs noirs y attirent "
        "souvent des regards curieux, surtout en dehors des zones touristiques centrales. La "
        "plupart des voyageurs y rapportent des interactions respectueuses, bien que "
        "réservées."
    ),
    "fukuoka-japan": (
        "Fukuoka est une ville compacte et en pleine croissance sur l'île méridionale de "
        "Kyushu, connue pour ses étals de rue (yatai), ses plages et un rythme de vie plus "
        "détendu qu'à Tokyo ou Osaka. Elle reçoit beaucoup moins de touristes étrangers, "
        "donc les voyageurs noirs doivent s'attendre à davantage de regards et à une "
        "présence diasporique ou expatriée plus restreinte, mais les cas d'hostilité "
        "ouverte restent rares et les habitants sont généralement décrits comme polis et "
        "curieux plutôt qu'inamicaux."
    ),
}

META_TEMPLATE_FR = (
    "{name} est-elle accueillante pour les voyageurs noirs ? "
    "Lisez les avis, découvrez le score d'accueil, trouvez des lieux à visiter."
)


def seed_descriptions_fr(apps, schema_editor):
    City = apps.get_model('cities', 'City')
    for slug, description_fr in DESCRIPTIONS_FR.items():
        try:
            city = City.objects.get(slug=slug)
        except City.DoesNotExist:
            continue
        city.description_fr = description_fr
        city.meta_description_fr = META_TEMPLATE_FR.format(name=city.name)
        city.save(update_fields=['description_fr', 'meta_description_fr'])


def clear_descriptions_fr(apps, schema_editor):
    City = apps.get_model('cities', 'City')
    City.objects.filter(slug__in=DESCRIPTIONS_FR.keys()).update(
        description_fr='', meta_description_fr=''
    )


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0018_seed_japan_cities'),
    ]

    operations = [
        migrations.RunPython(seed_descriptions_fr, clear_descriptions_fr),
    ]
