"""
Remove the User model from the accounts app state now that it lives in users.
No SQL is run — the accounts_user table is kept as-is.
"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_unique_email'),
        ('users', '0001_state_user'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel('User'),
            ],
            database_operations=[],
        ),
    ]
