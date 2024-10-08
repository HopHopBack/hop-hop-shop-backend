# Generated by Django 5.0.6 on 2024-09-22 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0006_merge_20240914_1136"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="phone_number",
            field=models.CharField(
                max_length=17,
                null=True,
                unique=True,
                verbose_name="phone number",
            ),
        ),
    ]
