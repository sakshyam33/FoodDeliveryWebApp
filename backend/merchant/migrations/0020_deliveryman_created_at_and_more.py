# Generated by Django 5.2 on 2025-05-10 14:20

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("merchant", "0019_remove_restaurant_city_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="deliveryman",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="restaurant",
            name="owner_contact",
            field=models.CharField(
                max_length=15,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Enter a valid Nepali mobile or landline number",
                        regex="^(?:((98|97|96)\\d{8})|(0\\d{2,3}\\d{6}))$",
                    )
                ],
            ),
        ),
    ]
