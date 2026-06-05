from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_groups_alter_user_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
        # Mark all existing users as verified so current accounts keep working.
        migrations.RunSQL(
            sql='UPDATE accounts_user SET email_verified = TRUE',
            reverse_sql='UPDATE accounts_user SET email_verified = FALSE',
        ),
    ]
