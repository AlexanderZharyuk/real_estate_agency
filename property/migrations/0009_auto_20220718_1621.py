# Generated by Django 2.2.24 on 2022-07-18 13:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_flat_liked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_flats', to=settings.AUTH_USER_MODEL),
        ),
    ]
