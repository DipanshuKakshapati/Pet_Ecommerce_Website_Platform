# Generated by Django 4.2.4 on 2023-09-12 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0022_remove_rating_user_remove_review_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="user",
        ),
    ]
