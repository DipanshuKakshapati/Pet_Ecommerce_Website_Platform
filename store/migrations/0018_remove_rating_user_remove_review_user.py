# Generated by Django 4.2.4 on 2023-09-12 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0017_vetdoctor_appointment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rating",
            name="user",
        ),
        migrations.RemoveField(
            model_name="review",
            name="user",
        ),
    ]
