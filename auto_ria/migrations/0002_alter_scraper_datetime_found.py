# Generated by Django 5.0.2 on 2024-02-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auto_ria", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scraper",
            name="datetime_found",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
