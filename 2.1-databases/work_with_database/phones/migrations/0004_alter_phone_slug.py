# Generated by Django 4.1 on 2022-08-04 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("phones", "0003_rename_lug_phone_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="phone", name="slug", field=models.SlugField(null=True),
        ),
    ]
