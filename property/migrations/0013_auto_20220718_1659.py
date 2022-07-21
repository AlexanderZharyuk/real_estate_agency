# Generated by Django 2.2.24 on 2022-07-18 13:38
from itertools import chain

from django.db import migrations
import phonenumbers


def clear_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats_iterator = Flat.objects.all().iterator()

    try:
        first_iterration = next(flats_iterator)
    except StopIteration:
        return None

    for flat in chain([first_iterration], flats_iterator):
        phone_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(phone_number):
            cleared_phone_number = phonenumbers.format_number(
                phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL
            )
            flat.owner_pure_phone = cleared_phone_number
        else:
            flat.owner_pure_phone = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20220718_1630'),
    ]

    operations = [
        migrations.RunPython(clear_phone_number)
    ]
