# Generated by Django 4.0.6 on 2022-08-04 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(default=False),
        ),
    ]
