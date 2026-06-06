from django.db import migrations, models


def copy_welcome_to_base(apps, schema_editor):
    City = apps.get_model('cities', 'City')
    City.objects.all().update(base_score=models.F('welcome_score'))


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0011_alter_place_google_place_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='base_score',
            field=models.DecimalField(
                max_digits=3,
                decimal_places=1,
                default=0.0,
                help_text='Editorial seed score (counts as 10 user votes in the weighted average)',
            ),
        ),
        migrations.RunPython(copy_welcome_to_base, migrations.RunPython.noop),
    ]
