from django.db import migrations

COUNTRY_TO_CONTINENT = {
    'France': 'Europe',
    'Spain': 'Europe',
    'United States': 'Americas',
    'China': 'Asia',
    'Italy': 'Europe',
    'Turkey': 'Europe',
    'Mexico': 'Americas',
    'Germany': 'Europe',
    'Thailand': 'Asia',
    'United Kingdom': 'Europe',
    'Ghana': 'Africa',
    'South Africa': 'Africa',
    'Brazil': 'Americas',
    'Portugal': 'Europe',
    'Senegal': 'Africa',
}


def assign_continents(apps, schema_editor):
    City = apps.get_model('cities', 'City')
    for country, continent in COUNTRY_TO_CONTINENT.items():
        City.objects.filter(country=country).update(continent=continent)


def clear_continents(apps, schema_editor):
    City = apps.get_model('cities', 'City')
    City.objects.all().update(continent='Europe')


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0005_city_continent'),
    ]

    operations = [
        migrations.RunPython(assign_continents, reverse_code=clear_continents),
    ]
