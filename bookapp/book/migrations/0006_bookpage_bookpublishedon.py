# Generated by Django 5.0.1 on 2024-01-07 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0005_rename_authordescription_authorpage_authordescription_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookpage",
            name="bookPublishedOn",
            field=models.DateField(blank=True, null=True),
        ),
    ]