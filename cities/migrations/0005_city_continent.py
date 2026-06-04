from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0004_add_hero_image_attribution'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='continent',
            field=models.CharField(
                choices=[
                    ('Africa', 'Africa'),
                    ('Americas', 'Americas'),
                    ('Asia', 'Asia'),
                    ('Europe', 'Europe'),
                    ('Middle East', 'Middle East'),
                    ('Oceania', 'Oceania'),
                ],
                db_index=True,
                default='Europe',
                max_length=20,
            ),
        ),
    ]
